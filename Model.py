from Layer import Dense, Layer
import numpy as np
from copy import copy
from Losses import MAE, MSE, CategoricalCrossEntroy, BinaryCrossEntropy
from Optimizer import SGD, MiniBatchGD
from tqdm import trange, tqdm

class Model(object):
	def __init__(self):
		super().__init__()
		self.layers = []
		self.optimizer = None
		self.loss_func = None

	def add(self, layer):
		if len(self.layers) >= 1:
			layer.prev_layer = self.layers[-1]
		self.layers.append(layer)
		

	def compile(self, loss, optimizer, lr=0.01):
		self.loss_func = {
			"mae": MAE(),
			"mse": MSE(),
			"cce": CategoricalCrossEntroy(),
			"bce": BinaryCrossEntropy()
		}[loss]

		self.optimizer = {
			"sgd": SGD(),
			"mini_batch_gd": MiniBatchGD(layers=self.layers, lr=lr)
		}[optimizer]


	def fit(self, X, Y, epochs, batch_size=32, shuffle=True):

		assert len(X) == len(Y)
		num_batches = int(np.ceil(len(X)/batch_size))
		losses = []
		for epoch in range(epochs):
			losse = 0
			t = trange(num_batches)
			for batch in t:
				if (batch+1)*batch_size < len(X):
					batch_x = X[batch*batch_size:(batch+1)*batch_size]
					batch_y = Y[batch*batch_size:(batch+1)*batch_size]
				else:
					batch_x = X[batch*batch_size:]
					batch_y = Y[batch*batch_size:]

				batch_loss = 0  # Thing to be minimized

				self.optimizer.reset_gradients(self.layers)

				for count, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
					x = x_ele.copy()

					# Forward pass the data
					for l in self.layers:
						x = l.compute_layer(x)

					# Calculating the loss : y_ele -> Truth, x -> network output
					x_loss = self.loss_func(y_ele, x)
					batch_loss += x_loss

					# Output layer error
					x_err = self.loss_func.der(y_ele, x) * \
						l.activation.der(l.weighted_sum)

					self.optimizer.update_gradients(self.layers, x_err)

					# ---------- FOR STOCHASTIC GRADIENT DESCENT -------------
					# self.optimizer.step(self.layers, 1)
					# --------------------------------------------------------


				batch_loss /= batch_size
				lossb = batch_loss.mean()
				losses.append(lossb)

				losse += lossb

				# t.set_description(f"EPOCH: {epoch+1} LOSS: {np.round(lossb, 3)}".format(x_loss))
				t.set_description(f"EPOCH: {epoch+1} LOSS: {lossb}".format(x_loss))
				t.refresh()

				# Update the weights & biases based on the calculated gradients
				self.optimizer.step(self.layers, len(batch_x))

			losse /= num_batches
			
		return np.asarray(losses)

	def predict(self, test_x):
		result = []

		for x in test_x:
			temp_x = x.copy()
			for l in self.layers:
				temp_x = l.compute_layer(temp_x)

			result.append(temp_x)

		return np.asarray(result)

	def __str__(self):
		ret = "------------------------------------------------\n"
		for i, l in enumerate(self.layers):
			ret += "Layer: " + str(i) + " Size: " + str(l.num_nodes) + "\n"
		ret += "------------------------------------------------\n"
		return ret

	def __iter__(self):
		for l in self.layers:
			yield l
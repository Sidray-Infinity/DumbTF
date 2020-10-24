from Layer import Dense
import numpy as np
from copy import copy
from Losses import MAE, MSE, CategoricalCrossEntroy
from Optimizer import SGD, MiniBatchGD
from tqdm import trange, tqdm

class Model(object):
	def __init__(self):
		super().__init__()
		self.layers = []
		self.optimizer = None
		self.loss_func = None

	def add(self, layer):
		self.layers.append(layer)

	def compile(self, loss, optimizer):
		"""----------------------------------------------
		Also include the weights initialization code here.
		-----------------------------------------------"""

		self.loss_func = {
			"mae": MAE(),
			"mse": MSE(),
			"cse": CategoricalCrossEntroy()
		}[loss]

		self.optimizer = {
			"sgd": SGD(),
			"mini_batch_gd": MiniBatchGD()
		}[optimizer]


	def fit(self, X, Y, epochs, batch_size=32, shuffle=True, lr=0.001):

		assert len(X) == len(Y)
		num_batches = int(np.ceil(len(X)/batch_size))
		losses = []
		for epoch in range(epochs):
			losse = 0
			t = trange(num_batches)
			# for i in tqdm(range(num_batches)):
			for batch in t:
				if (batch+1)*batch_size < len(X):
					batch_x = X[batch*batch_size:(batch+1)*batch_size]
					batch_y = Y[batch*batch_size:(batch+1)*batch_size]
				else:
					batch_x = X[batch*batch_size:]
					batch_y = Y[batch*batch_size:]

				batch_loss = 0  # Thing to be minimized

				batch_weight_grads = np.asarray([np.zeros(l.weights.shape) for l in self.layers])
				batch_biases_grads = np.asarray([np.zeros(l.biases.shape) for l in self.layers])

				for j, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
					x = x_ele.copy()

					# Forward pass the data
					for l in self.layers:
						x = l.compute_layer(x)

					# Calculating the loss : y_ele -> Truth, x -> network output
					x_loss = self.loss_func(y_ele, x)

					# Output layer error
					x_err = self.loss_func.der(y_ele, x) * \
						l.activation.der(l.weighted_sum)


					for i in range(len(self.layers)-1, 0, -1):

						batch_biases_grads[i] += x_err

						# for k1 in range(c):
						# 	for k2 in range(self.layers[i].num_nodes):
						# 		self.batch_weight_grads[i][k2] += \
						# 			self.layers[i-1].output[k1]*x_err[k2]

					
						batch_weight_grads[i] += np.multiply.outer(x_err, self.layers[i-1].output)


					    # Calculating error for the layer below
						x_err = (self.layers[i].weights.T @ x_err) * \
							self.layers[i-1].activation.der(
							self.layers[i-1].weighted_sum)

					# Update the weights & biases based on the calculated gradients
					# ------------ FOR STOCHASTIC GRADIENT DESCENT ----------------
					# for i in range(len(self.layers)-1, 0, -1):
					# 	self.layers[i].weights -= lr * self.batch_weight_grads[i]
					# 	self.layers[i].biases -= lr * self.batch_biases_grads[i]
					# -------------------------------------------------------------

					batch_loss += x_loss


				"""---------------------------------------------------
				- Finding the gradient wrt to batch loss.
				- Trying to update the weights and biases based on the
					gradients.
				---------------------------------------------------"""
				batch_loss /= batch_size
				batch_weight_grads /= batch_size
				batch_biases_grads /= batch_size
				lossb = batch_loss.mean()
				losse += lossb

				t.set_description(f"EPOCH: {epoch} LOSS: {lossb}".format(x_loss))
				t.refresh()
				# Update the weights & biases based on the calculated gradients
	
				for i in range(len(self.layers)-1, 0, -1):
					self.layers[i].weights -= lr * batch_weight_grads[i]
					self.layers[i].biases -= lr * batch_biases_grads[i]

			losse /= num_batches
			losses.append(losse)
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
from Layer import Layer
import numpy as np
from copy import copy
from Losses import MAE, MSE, CategoricalCrossEntroy
from Optimizer import SGD, MiniBatchGD
from tqdm import tqdm

from sklearn.datasets import load_boston
import tensorflow as tf
import pandas as pd

class Model(object):
	def __init__(self):
		super().__init__()
		self.layers = []
		self.optimizer = None
		self.loss_func = None

	def add(self, layer: Layer):
		self.layers.append(layer)

	def compile(self, loss, optimizer):
		"""----------------------------------------------
		Also include the weights initialization code here.
		-----------------------------------------------"""

		self.batch_weight_grads = np.array([np.zeros(l.weights.shape) for l in self.layers])
		self.batch_biases_grads = np.array([np.zeros(l.biases.shape) for l in self.layers])

		self.loss_func = {
			"mae": MAE(),
			"mse": MSE(),
			"cse": CategoricalCrossEntroy()
		}[loss]

		self.optimizer = {
			"sgd": SGD(),
			"mini_batch_gd": MiniBatchGD()
		}[optimizer]

	def forward_pass(self, data):
		"""-----------------------------
		Shift the forward pass code here.
		------------------------------"""

	def fit(self, X, Y, epochs, batch_size=1, shuffle=True, lr=0.001):

		assert len(X) == len(Y)

		num_batches = int(np.ceil(len(X)/batch_size))
		losses = []
		for epoch in range(epochs):
			print("EPOCH:", epoch)
			for i in range(num_batches):
				if (i+1)*batch_size < len(X):
					batch_x = X[i*batch_size:(i+1)*batch_size]
					batch_y = Y[i*batch_size:(i+1)*batch_size]
				else:
					batch_x = X[i*batch_size:]
					batch_y = Y[i*batch_size:]

				batch_loss = 0  # Thing to be minimized

				"""---------------------------------------------------------------------------------------------
				- Remove that first layer weight matrix. Not needed. Remember to update the indices in the logic.
				----------------------------------------------------------------------------------------------"""



				for j, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
					x = x_ele.copy()
					# Forward pass the data
					for k, l in enumerate(self.layers):
						x = l.compute_layer(x)
						# print("EPOCH:", epoch, "BATCH IDX:",
						#       i, "BATCH ELE:", j, "LAYER:", k)

					x_loss = np.array(self.loss_func(y_ele, x))

					# Output layer error
					x_err = self.loss_func.der(y_ele, x) * \
						l.activation.der(l.weighted_sum)

					for i in range(len(self.layers)-1, 0, -1):

						self.batch_biases_grads[i] += x_err
						for k1 in range(self.layers[i-1].num_nodes):
							for k2 in range(self.layers[i].num_nodes):
								self.batch_weight_grads[i][k2] += \
									self.layers[i-1].output[k1]*x_err[k2]

						x_err = (self.layers[i].weights.T @ x_err) * \
							self.layers[i-1].activation.der(
							self.layers[i-1].weighted_sum)

					batch_loss += x_loss

				"""---------------------------------------------------
				- Finding the gradient wrt to batch loss.
				- Trying to update the weights and biases based on the
					gradients.
				---------------------------------------------------"""
				batch_loss /= batch_size
				self.batch_weight_grads /= batch_size
				self.batch_biases_grads /= batch_size
				lossb = batch_loss.mean()
				print(lossb)

				for i in range(len(self.layers)-1, 0, -1):
					self.layers[i].weights -= lr * self.batch_weight_grads[i]
					self.layers[i].biases -= lr * self.batch_biases_grads[i]

				losses.append(lossb)

		return losses

	def predict(self, test_x):
		result = []

		for x in test_x:
			temp_x = x.copy()
			for k, l in enumerate(self.layers):
				temp_x = l.compute_layer(temp_x)

			result.append(temp_x)

		return np.asarray(result)

	def __str__(self):
		ret = "------------------------------------------------\n"
		for i, l in enumerate(self.layers):
			ret += "Layer: " + str(i) + " Size: " + str(l.num_nodes) + "\n"
		ret += "------------------------------------------------\n"
		return ret


if __name__ == "__main__":

	dataset = load_boston()
	print(dataset.keys())
	df = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
	df['y'] = dataset['target']
	print(df.drop('y', axis=1).columns)

	# exit()
	# model_tf = tf.keras.Sequential([
	# 	tf.keras.layers.Dense(50, input_shape=df.drop('y', axis=1).shape, activation='relu'),
	# 	tf.keras.layers.Dense(100, activation='relu'),
	# 	tf.keras.layers.Dense(50, activation='relu'),
	# 	tf.keras.layers.Dense(1)
	# ])

	# model_tf.compile(optimizer="adam", loss="mse", metrics=["mse", "mae"])
	# model_tf.fit(df.drop('y', axis=1), df['y'], epochs=500)

	model = Model()
	model.add(Layer(50, input_shape=13, activation='relu'))
	model.add(Layer(100, input_shape=50, activation='relu'))
	model.add(Layer(50, input_shape=100, activation='relu'))
	model.add(Layer(1, input_shape=50, activation='linear'))

	X = np.asarray(df.drop('y', axis=1))
	Y = np.asarray(df['y'])

	model.compile(loss="mse", optimizer="mini_batch_gd")
	loss = model.fit(X, Y, batch_size=32, epochs=500)
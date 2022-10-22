from layer import Layer
from activation.activations import ReLU, Sigmoid, Linear, Softmax
import numpy as np


class Dense(Layer):
    def __init__(self, num_nodes, input_shape, activation):
        super().__init__()
        self.prev_layer = None
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid(),
            'linear': Linear(),
            'softmax': Softmax()
        }[activation]

        # ************* He initialization ***************
        self.weights = np.random.randn(self.num_nodes, input_shape).astype(
            np.float32) * np.sqrt(2 / input_shape)
        self.biases = np.zeros(shape=self.num_nodes, ).astype(np.float32)
        self.weighted_sum = np.empty(shape=self.num_nodes).astype(np.float32)
        self.output = []

        # DS's to hold the gradients while backprop
        self.weight_grads = np.zeros(
            (self.num_nodes, self.input_shape)).astype(np.float32)
        self.biases_grads = np.zeros(self.num_nodes).astype(np.float32)

    def reset_gradients(self):
        self.weight_grads = np.zeros(
            (self.num_nodes, self.input_shape)).astype(np.float32)
        self.biases_grads = np.zeros(shape=self.num_nodes).astype(np.float32)

    def update_gradients(self, error):
        if self.prev_layer is None:
            return

        self.biases_grads += error
        self.weight_grads += np.multiply.outer(error, self.prev_layer.output)

        curr_error = (self.weights.T @ error) * \
                     self.prev_layer.activation.der(
                         self.prev_layer.weighted_sum)

        return curr_error

    def backward(self, lr, batch_size):
        self.weight_grads /= batch_size
        self.biases_grads /= batch_size

        self.weights -= lr * self.weight_grads
        self.biases -= lr * self.biases_grads

    def compute_layer(self, input_data):
        self.weighted_sum = self.weights @ input_data + self.biases
        self.output = self.activation(self.weighted_sum)

        return self.output

    def __iter__(self):
        for node in zip(self.weights, self.biases):
            yield node

    def __str__(self):
        return f"NUM NODES: {self.num_nodes} ACTIVATON: {self.activation}" + \
               f"INPUT SHAPE: {self.input_shape}"

    def __call__(self, x):
        return self.compute_layer(x)

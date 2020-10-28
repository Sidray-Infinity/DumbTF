import numpy as np
from Activations import ReLU, Sigmoid, Linear, Softmax

class Layer(object):
    def __init__(self):
        super().__init__()


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
        self.weights = np.random.randn(self.num_nodes, input_shape) * np.sqrt(2/input_shape)
        self.biases = np.zeros(shape=self.num_nodes)
        self.weighted_sum = np.empty(shape=self.num_nodes, dtype=float)
        self.output = []

        self.weight_grads = np.zeros((self.num_nodes, self.input_shape))
        self.biases_grads = np.zeros(shape=self.num_nodes)

    def reset_gradients(self):
        self.weight_grads = np.zeros((self.num_nodes, self.input_shape))
        self.biases_grads = np.zeros(shape=self.num_nodes)

    def update_gradients(self, error):
        if self.prev_layer is None:
            return

        self.biases_grads += error
        self.weight_grads += np.multiply.outer(error, self.prev_layer.output)

        curr_error = (self.weights.T @ error) * \
                self.prev_layer.activation.der(
                self.prev_layer.weighted_sum)

        return curr_error

    def update_params(self, lr, batch_size):
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
        return f"NUM NODES: {self.num_nodes} ACTIVATON: {self.activation}" +\
            f"INPUT SHAPE: {self.input_shape}"

class Conv2D(Layer):
    def __init__(self, filters, kernel_size, activation, input_shape, stride=(1, 1)):
        super.__init__()
        self.filters = filters
        self.kernel_size = kernel_size
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid(),
            'linear': Linear(),
            'softmax': Softmax()
        }[activation]

        self.op_H = (input_shape[0] - kernel_size) // stride[0] + 1
        self.op_W = (input_shape[1] - kernel_size) // stride[1] + 1
        self.output = np.zeros((filters, self.op_H, self.op_W))

        self.kernels = np.random.randn(filters, kernel_size, kernel_size)

    def compute_layer(self, input_data):
        pass
import numpy as np
from Activations import ReLU, Sigmoid, Linear


class Layer(object):
    def __init__(self, num_nodes, input_shape, activation):
        super().__init__()
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid(),
            'linear': Linear()
        }[activation]

        self.weights = np.random.randn(self.num_nodes, input_shape)
        self.biases = np.zeros(shape=self.num_nodes)
        self.weighted_sum = np.empty(shape=self.num_nodes, dtype=float)
        self.output = []

    def compute_layer(self, input_data):
        # print(self.weights.shape, input_data.shape)
        self.weighted_sum = self.weights @ input_data + self.biases
        self.output = self.activation(self.weighted_sum)

        return self.output

    def __iter__(self):
        # print(self.weights)
        for node in zip(self.weights, self.biases):
            yield node

    def __str__(self):
        return "NUM NODES: " + str(self.num_nodes)


if __name__ == "__main__":
    a = np.array([13, 14, 15, 16])
    l = Layer(3, 4, activation='relu')
    l()
    a = l.compute_layer(a)
    print('\n', a)

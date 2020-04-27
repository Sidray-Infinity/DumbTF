import numpy as np
from Activations import ReLU, Sigmoid


class Node(object):
    def __init__(self, input_size, activation):
        super().__init__()
        self.weights = np.random.normal(0, 1, size=input_size)
        self.bias = 0
        self.weighted_sum = None
        self.output = None
        self.activation = activation

    def __str__(self):
        return "WEIGHT: " + str(self.weights) + \
            "\n BIAS: " + str(self.bias) + \
            "\n O/P: " + str(self.output)

    def compute(self, input_data):

        self.weighted_sum = np.dot(self.weights, input_data) + self.bias
        self.output = self.activation(self.weighted_sum)

        return self.output


if __name__ == "__main__":
    n = Node(32, 64)

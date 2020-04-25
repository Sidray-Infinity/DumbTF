import numpy as np


class Node(object):
    def __init__(self, input_size, activation='relu'):
        super().__init__()
        self.weights = np.array([np.random.randn() for _ in range(input_size)])
        self.bias = 0
        self.output = None
        self.activation = activation

    def __str__(self):
        return "WEIGHT: " + str(self.weights) + "\n BIAS: " + str(self.bias) + "\n O/P: " + str(self.output)

    def apply_activation(self, data):

        if self.activation == 'relu':
            return data if data > 0 else 0

    def compute(self, input_data):

        self.output = self.apply_activation(
            np.dot(self.weights, input_data) + self.bias)

        return self.output


if __name__ == "__main__":
    n = Node(32, 64)

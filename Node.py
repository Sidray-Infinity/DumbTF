import numpy as np


class Node(object):
    def __init__(self, input, output):
        super().__init__()
        self.weights = np.random.randn()
        self.bias = 0

    def __str__(self):
        return "WEIGHT: " + str(self.weights) + " BIAS: " + str(self.bias)


if __name__ == "__main__":
    n = Node(32, 64)

import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return data if data > 0 else 0

    def derivative(self, data):
        return 1 if data > 0 else 0


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return np.exp(data) / (np.exp(data) + 1)

    def derivative(self, data):
        return 1 if data > 0 else 0


if __name__ == "__main__":

    pass

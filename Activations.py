import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        data[data <= 0] = 0
        return data

    def der(self, data):
        data[data <= 0] = 0
        data[data > 0] = 1
        return data


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return 1 / (1 + np.exp(-data))

    def der(self, data):

        return (1 / (1 + np.exp(-data))) * (1 - 1 / (1 + np.exp(-data)))


if __name__ == "__main__":

    pass

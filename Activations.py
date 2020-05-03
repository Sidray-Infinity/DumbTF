import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        data[data < 0] = 0
        return data

    def der(self, data):
        return 1 if data > 0 else 0


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return np.exp(data) / (np.exp(data) + 1)

    def der(self, data):
        return (np.exp(data) / (np.exp(data) + 1)) - \
            (np.exp(2 * data) / (np.exp(data) + 1) ** 2)


if __name__ == "__main__":

    pass

import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        data[data < 0] = 0
        return data

    def der(self, data):
        for i in range(len(data)):
            if data[i] > 0:
                data[i] = 1
            else:
                data[i] = 0
        return data


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return np.exp(data) / (np.exp(data) + 1)

    def der(self, data):
        print("DATA", (np.exp(data) / (np.exp(data) + 1)) -
              (np.exp(2 * data) / (np.exp(data) + 1) ** 2))
        return (np.exp(data) / (np.exp(data) + 1)) - \
            (np.exp(2 * data) / (np.exp(data) + 1) ** 2)


if __name__ == "__main__":

    pass

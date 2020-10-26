import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return np.maximum(0, data)

    def der(self, data):

        data = np.maximum(0, data)
        data[data > 0] = 1
        return data


class Linear(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return data

    def der(self, data):
        return np.ones(data.shape, dtype='float32')


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def sigmoid(self, data):
        """
        For numerical stability
        """
        sig = np.zeros_like(data)
        for i in range(len(data)):
            if data[i] < 0:
                a = np.exp(data[i])
                sig[i] = a/(1+a)
            else:
                sig[i] = 1 / (1 + np.exp(-data[i]))

  
        sig = np.minimum(sig, 0.999999)  # Set upper bound
        sig = np.maximum(sig, 0.000001)  # Set lower bound
        return sig


    def __call__(self, data):
        return self.sigmoid(data)


    def der(self, data):
        return self.sigmoid(data) * (1.0 - self.sigmoid(data))


class Softmax(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        """
        * data -> Layer output 1D array
        * For numerical stability
        """
        shift_data = data - np.max(data)
        exps = np.exp(shift_data)
        return exps/np.sum(exps)


    def der(self):
        pass


if __name__ == "__main__":

    pass

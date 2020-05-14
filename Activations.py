import numpy as np


class ReLU(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        data[data < 0] = 0
        return data

    def der(self, data):
        data[data <= 0] = 0
        data[data > 0] = 1
        return data


class Linear(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return data

    def der(self, data):
        return 1


class Sigmoid(object):
    def __init__(self):
        super().__init__()

    def sigmoid(self, data):
        """
        For numerical stability
        """
        for i in range(len(data)):
            if data[i] < 0:
                a = np.exp(data[i])
                data[i] = a/(1+a)
            else:
                data[i] = 1 / (1 + np.exp(-data[i]))

        """------------------------------------------------------------------------------------
        - Contemplate whether to convert it to probability here, or in the __call__ function ??
        ------------------------------------------------------------------------------------"""

        data /= data.sum()
        return data

    def __call__(self, data):
        data = self.sigmoid(data)
        return data

    def der(self, data):
        return self.sigmoid(data) * (1 - self.sigmoid(data))


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

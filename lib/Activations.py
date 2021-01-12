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

    def __str__(self):
        return 'ReLU '


class Linear(object):
    def __init__(self):
        super().__init__()

    def __call__(self, data):
        return data

    def der(self, data):
        return np.ones(data.shape, dtype='float32')
    
    def __str__(self):
        return 'Linear '


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

        sig = np.minimum(sig, 0.9999999999999)  # Set upper bound
        sig = np.maximum(sig, 0.0000000000001)  # Set lower bound
        return sig
    
    def __call__(self, data):
        return self.sigmoid(data)


    def der(self, data):
        return self.sigmoid(data) * (1.0 - self.sigmoid(data))

    def __str__(self):
        return 'Sigmoid '

class Softmax(object):
    def __init__(self,):
        super().__init__()

    def __call__(self, data):
        shift_data = data - np.max(data) # For numerical stability

        exps = np.exp(shift_data)
        res = exps / np.sum(exps)
        res = np.minimum(res, 0.9999999999999)  # Set upper bound
        res = np.maximum(res, 0.0000000000001)  # Set lower bound
        return res
        
    def der(self, data):
        # For numerical stability
        shift_data = data - np.max(data)
        totalSum = np.sum(np.exp(shift_data))
        totalSumSqr = totalSum ** 2
        res = np.zeros_like(shift_data)
        for i in range(shift_data.shape[0]):
            currExp = np.exp(shift_data[i])
            res[i] = ((totalSum - currExp) * currExp) / totalSumSqr

        return res

    def __str__(self):
        return 'Softmax '
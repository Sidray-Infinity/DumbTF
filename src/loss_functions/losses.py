import numpy as np


class MAE(object):
    def __init__(self, y_true=None, y_pred=None):

        super().__init__()
        self.y_pred = y_pred
        self.y_true = y_true

    def der(self, y_true, y_pred):
        ret = np.ones(y_pred.shape)
        for i in range(y_pred.shape[0]):
            if y_pred - y_true < 0:
                ret[i] *= -1
        return ret

    def __call__(self, y_true, y_pred):
        return abs(y_true - y_pred)


class BinaryCrossEntropy(object):
    def __init__(self):
        pass

    def __call__(self, y_true, y_pred):
        if y_true == 1:
            return -np.log(y_pred[0])

        return -np.log(1 - y_pred[0])

    def der(self, y_true, y_pred):
        return (y_pred[0] - y_true) / (y_pred[0] - y_pred[0] * y_pred[0])


class CategoricalCrossEntroy(object):

    def __init__(self, y_true=None, y_pred=None):
        super().__init__()

    def der(self, y_true, y_pred):

        res = np.zeros_like(y_true)
        sum_ = np.sum(y_pred)
        true_index = np.argmax(y_true)
        for i in range(y_true.shape[0]):
            if i == true_index:
                res[i] = y_pred[i] - 1
            else:
                res[i] = y_pred[i]
        return res

    def __call__(self, y_true, y_pred):
        """
        * Ensure that the target vector is one-hot encoded
        * Ensure that the final layer activation is softmax
        """
        return -np.log(y_pred[np.argmax(y_true)])


class MSE(object):
    def __init__(self, y_true=None, y_pred=None):
        super().__init__()
        self.y_pred = y_pred
        self.y_true = y_true

    def der(self, y_true, pred):
        return np.asarray(pred - y_true)

    def __call__(self, y_true, y_pred):
        # Accoring to https://brilliant.org/wiki/backpropagation/#$
        # Turns out, the 0.5 helps during back propagation
        return np.asarray(0.5 * ((y_true - y_pred) ** 2))

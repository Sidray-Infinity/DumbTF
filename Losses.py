import numpy as np


class MAE(object):
    def __init__(self, y_true=None, y_pred=None):

        super().__init__()
        self.y_pred = y_pred
        self.y_true = y_true

    def __call__(self, y_true, y_pred):
        return np.mean(abs(y_true - y_pred))


class CategoricalCrossEntroy(object):

    def __init__(self):
        super().__init__()


class MSE(object):
    def __init__(self, y_true=None, y_pred=None):
        super().__init__()
        self.y_pred = y_pred
        self.y_true = y_true

    def der(self, y_true, pred):
        return pred - y_true

    def __call__(self, y_true, y_pred):
        # Accoring to https://brilliant.org/wiki/backpropagation/#$
        # Turns out, the 0.5 helps during back propagation
        return 0.5 * (abs(y_true - y_pred) ** 2)


if __name__ == "__main__":
    pass

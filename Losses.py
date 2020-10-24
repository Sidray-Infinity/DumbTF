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
                ret[i]*= -1
        return ret

    def __call__(self, y_true, y_pred):
        return abs(y_true - y_pred)


class CategoricalCrossEntroy(object):

    def __init__(self, y_true=None, y_pred=None):
        super().__init__()
        self.y_pred = y_pred
        self.y_true = y_true

    def der(self, y_true, y_pred):
        """
        The derivative wrt to the positive class and the negative class are different.
        """
        true_class_index = np.argmax(y_true)
        pos_score = y_pred[true_class_index]
        e_sum = np.sum(np.exp(y_pred))
        der = []
        for i in range(len(y_true)):
            if i != true_class_index:
                der.append(np.exp(y_pred[i])/e_sum)  # For all other classes
            else:
                # For the positive class
                der.append(np.exp(pos_score)/e_sum - 1)

        return np.asarray(der)

    def __call__(self, y_true, y_pred):
        """
        * Ensure that the target vector is one-hot encoded
        * Ensure that the final layer activation is softmax
        """

        pos_score = y_pred[np.argmax(y_true)]
        e_sum = np.sum(np.exp(y_pred))

        return np.asarray(-1 * np.log(np.exp(pos_score)/e_sum))


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


if __name__ == "__main__":
    pass

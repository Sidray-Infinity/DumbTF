import numpy as np


class MiniBatchGD(object):
    def __init__(self):
        super().__init__()
        self.batch_weight_grads = np.array(
            [np.zeros(l.weights.shape) for l in self.layers])
        self.batch_biases_grads = np.array(
            [np.zeros(l.biases.shape) for l in self.layers])

    def optimize(self, x_loss, x_err):
        """
        * x_loss -> loss of the forward pass
        * x_err -> Error of the final layer
        """
        pass


class SGD(object):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    pass

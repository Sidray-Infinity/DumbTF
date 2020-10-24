import numpy as np


class MiniBatchGD(object):
    def __init__(self):
        super().__init__()

    def step(self, x_loss, x_err, batch_weight_grads, batch_biases_grads):
        """
        * x_loss -> loss of the forward pass
        * x_err -> Error of the final layer
        """
        pass


class SGD(object):
    def __init__(self):
        super().__init__()

    def step(self):
        """
        * x_loss -> loss of the forward pass
        * x_err -> Error of the final layer
        """
        pass


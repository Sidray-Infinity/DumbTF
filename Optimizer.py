import numpy as np


class MiniBatchGD(object):
    def __init__(self, layers, lr):
        super().__init__()
        self.lr = lr
    
    def reset_gradients(self, layers):
        for l in layers:
            l.reset_gradients()

    def update_gradients(self, layers, error):
        for i in range(len(layers)-1, 0, -1):
            error = layers[i].update_gradients(error)


    def step(self, layers, batch_size):
        for l in layers:
            l.update_params(self.lr, batch_size)

class SGD(object):
    def __init__(self):
        super().__init__()

    def step(self):
        """
        * x_loss -> loss of the forward pass
        * x_err -> Error of the final layer
        """
        pass


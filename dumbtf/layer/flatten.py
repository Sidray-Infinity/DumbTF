import numpy as np

from activation.activations import Linear
from layer import Layer


class Flatten(Layer):
    def __init__(self, input_shape=None):
        super().__init__()
        self.input_shape = None
        self.prev_layer = None
        self.output = None
        self.weighted_sum = None
        self.activation = Linear()

    def compute_layer(self, input_data):
        self.output = np.asarray(input_data).flatten()
        self.weighted_sum = self.output
        return self.output

    def reset_gradients(self):
        pass

    def update_gradients(self, error):
        return error.reshape(self.prev_layer.output.shape)

    def backward(self, lr, batch_size):
        pass

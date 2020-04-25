from Node import Node
from Layer import Layer
import numpy as np


class Model(object):
    def __init__(self):
        super().__init__()
        self.layers = []

    def add(self, layer: Layer):
        self.layers.append(layer)

    def fit(self, x, y, epochs, batch_size, shuffle=True):
        for i, l in enumerate(self.layers):
            x = l.compute_layer(x)
            print(i, len(x), x)
        return x


if __name__ == "__main__":

    model = Model()
    model.add(Layer(4, 4))
    model.add(Layer(6, 4))
    model.add(Layer(5, 6))

    model.fit([1, 2, 3, 4], None, None, None)

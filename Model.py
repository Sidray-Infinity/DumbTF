from Node import Node
from Layer import Layer
import numpy as np
from copy import copy
import math


class Model(object):
    def __init__(self):
        super().__init__()
        self.layers = []

    def add(self, layer: Layer):
        self.layers.append(layer)

    def fit(self, x, y, epochs, batch_size=1, shuffle=True):

        num_batches = math.ceil(len(x)/batch_size)

        for epoch in range(epochs):
            for i in range(num_batches):
                if (i+1)*batch_size < len(x):
                    batch_x = x[i*batch_size:(i+1)*batch_size]
                    batch_y = y[i*batch_size:(i+1)*batch_size]
                else:
                    batch_x = x[i*batch_size:]
                    batch_y = y[i*batch_size:]

                for j, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
                    b = x_ele.copy()
                    for k, l in enumerate(self.layers):
                        b = l.compute_layer(b)
                        print("EPOCH:", epoch, "BATCH IDX:",
                              i, "BATCH ELE:", j, "LAYER:", k)

        return b

    def __str__(self):
        ret = "------------------------------------------------\n"
        for i, l in enumerate(self.layers):
            ret += "Layer: " + str(i) + " Size: " + str(l.num_nodes) + "\n"
        ret += "------------------------------------------------\n"
        return ret


if __name__ == "__main__":

    model = Model()
    model.add(Layer(4, 4))
    model.add(Layer(6, 4))
    model.add(Layer(3, 6))
    print(model)

    input_ = np.asarray([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    output = np.asarray([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ])

    print(model.fit(input_, output, epochs=1, batch_size=2))

from Node import Node
import numpy as np
from Activations import ReLU, Sigmoid


class Layer(object):
    def __init__(self, num_nodes, input_shape, activation):
        super().__init__()
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid()
        }[activation]
        self.nodes = [Node(input_shape, self.activation)
                      for _ in range(self.num_nodes)]
        self.output = []

    def compute_layer(self, input_data):
        self.output = []
        for node in self:
            self.output.append(node.compute(input_data))

        """ -----------------------------------------------
        For sigmoid/softmax activation, handle the sum == 1
        if isinstance(self.activation, Sigmoid):
            self.output /= sum(self.output)
        ------------------------------------------------"""

        return np.array(self.output)

    def __iter__(self):
        for node in self.nodes:
            yield node

    def __str__(self):
        return "NUM NODES: " + str(self.num_nodes)


if __name__ == "__main__":
    pass

from Node import Node
import numpy as np


class Layer(object):
    def __init__(self, num_nodes, input_shape, activation='relu'):
        super().__init__()
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.activation = activation
        self.nodes = [Node(input_shape, activation)
                      for _ in range(self.num_nodes)]
        self.output = []

    def compute_layer(self, input_data):

        for node in self:
            self.output.append(node.compute(input_data))

        return np.array(self.output)

    def __iter__(self):
        for node in self.nodes:
            yield node

from Node import Node


class Layer(object):
    def __init__(self, num_nodes, input_shape, output_shape, activation='relu'):
        super().__init__()
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.nodes = [Node(input_shape, output_shape)
                      for _ in range(self.num_nodes)]
        self.activation = activation

    def apply_activation(self, data):
        result = []
        if self.activation == 'relu':
            for d in data:
                result.append(max(d, 0))

        return result

    def compute(self, inputs):
        """
        Apply computation on the output of the previous layer output
        """
        assert len(inputs) == self.input_shape
        output = []
        for i in range(input_shape):
            output.append(self.nodes[i].weights *
                          inputs[i] + self.nodes[i].bias)

        return apply_activation(output)

    def __iter__(self):
        for node in self.nodes:
            yield node

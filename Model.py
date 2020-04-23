from Node import Node
from Layer import Layer


class Model(object):
    def __init__(self):
        super().__init__()
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)


if __name__ == "__main__":
    l = Layer(10, 5, 15)
    for d in l:
        print(d)

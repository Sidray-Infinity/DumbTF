from Layer import Layer
import numpy as np
from copy import copy
from Losses import MAE, MSE
from Optimizer import SGD, SimpleGD
import math


class Model(object):
    def __init__(self):
        super().__init__()
        self.layers = []
        self.optimizer = None
        self.loss_func = None

    def add(self, layer: Layer):
        self.layers.append(layer)

    def compile(self, loss, optimizer):
        """----------------------------------------------
        Also include the weights initialization code here.
        -----------------------------------------------"""

        if loss == "mae":
            self.loss_func = MAE()
        elif loss == "mse":
            self.loss_func = MSE()

        if optimizer == "sgd":
            self.optimizer = SGD()
        elif optimizer == "simple_sgd":
            self.optimizer = SimpleGD()

    def forward_pass(self, data):
        """-----------------------------
        Shift the forward pass code here.
        ------------------------------"""

    def fit(self, X, Y, epochs, batch_size=1, shuffle=True, lr=0.001):

        assert len(X) == len(Y)

        num_batches = math.ceil(len(X)/batch_size)

        for epoch in range(epochs):
            for i in range(num_batches):
                if (i+1)*batch_size < len(X):
                    batch_x = X[i*batch_size:(i+1)*batch_size]
                    batch_y = Y[i*batch_size:(i+1)*batch_size]
                else:
                    batch_x = X[i*batch_size:]
                    batch_y = Y[i*batch_size:]

                batch_loss = 0  # Thing to be minimized

                for j, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
                    x = x_ele.copy()
                    # Forward pass the data
                    for k, l in enumerate(self.layers):
                        x = l.compute_layer(x)
                        print("EPOCH:", epoch, "BATCH IDX:",
                              i, "BATCH ELE:", j, "LAYER:", k)

                    # Adding the loss of all elements of a batch
                    batch_loss += np.array(self.loss_func(y_ele, x))

                """---------------------------------------------------
                - Finding the gradient wrt to batch loss.
                - Trying to update the weights and biases based on the 
                  gradients.
                ---------------------------------------------------"""
                batch_loss /= batch_size

    def __str__(self):
        ret = "------------------------------------------------\n"
        for i, l in enumerate(self.layers):
            ret += "Layer: " + str(i) + " Size: " + str(l.num_nodes) + "\n"
        ret += "------------------------------------------------\n"
        return ret


if __name__ == "__main__":

    model = Model()
    model.add(Layer(4, 4, activation='relu'))
    model.add(Layer(6, 4, activation='relu'))
    model.add(Layer(3, 6, activation='sigmoid'))
    print(model)

    input_ = np.asarray([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [-1, -2, -3, -4]
    ])

    output = np.asarray([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [-1, -2, -3]
    ])

    model.compile(loss="mse", optimizer="simple_sgd")

    model.fit(input_, output, epochs=1, batch_size=2)

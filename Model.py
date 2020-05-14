from Layer import Layer
import numpy as np
from copy import copy
from Losses import MAE, MSE
from Optimizer import SGD, MiniBatchGD
from tqdm import tqdm


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

        self.loss_func = {
            "mae": MAE(),
            "mse": MSE()
        }[loss]

        self.optimizer = {
            "sgd": SGD(),
            "mini_batch_gd": MiniBatchGD()
        }[optimizer]

    def forward_pass(self, data):
        """-----------------------------
        Shift the forward pass code here.
        ------------------------------"""

    def fit(self, X, Y, epochs, batch_size=1, shuffle=True, lr=0.001):

        assert len(X) == len(Y)

        num_batches = np.ceil(len(X)/batch_size)
        losses = []
        for epoch in range(epochs):
            print("EPOCH:", epoch)
            for i in tqdm(range(num_batches)):
                if (i+1)*batch_size < len(X):
                    batch_x = X[i*batch_size:(i+1)*batch_size]
                    batch_y = Y[i*batch_size:(i+1)*batch_size]
                else:
                    batch_x = X[i*batch_size:]
                    batch_y = Y[i*batch_size:]

                batch_loss = 0  # Thing to be minimized

                """---------------------------------------------------------------------------------------------
				- Remove that first layer weight matrix. Not needed. Remember to update the indices in the logic.
				----------------------------------------------------------------------------------------------"""

                batch_weight_grads = np.array(
                    [np.zeros(l.weights.shape) for l in self.layers])
                batch_biases_grads = np.array(
                    [np.zeros(l.biases.shape) for l in self.layers])

                for j, (x_ele, y_ele) in enumerate(zip(batch_x, batch_y)):
                    x = x_ele.copy()
                    # Forward pass the data
                    for k, l in enumerate(self.layers):
                        x = l.compute_layer(x)
                        # print("EPOCH:", epoch, "BATCH IDX:",
                        #       i, "BATCH ELE:", j, "LAYER:", k)

                    x_loss = np.array(self.loss_func(y_ele, x))

                    # Output layer error
                    x_err = self.loss_func.der(y_ele, x) * \
                        l.activation.der(l.weighted_sum)

                    for i in range(len(self.layers)-1, 0, -1):

                        batch_biases_grads[i] += x_err
                        for k1 in range(self.layers[i-1].num_nodes):
                            for k2 in range(self.layers[i].num_nodes):
                                batch_weight_grads[i][k2] += \
                                    self.layers[i-1].output[k1]*x_err[k2]

                        x_err = (self.layers[i].weights.T @ x_err) * \
                            self.layers[i-1].activation.der(
                            self.layers[i-1].weighted_sum)

                    batch_loss += x_loss

                """---------------------------------------------------
				- Finding the gradient wrt to batch loss.
				- Trying to update the weights and biases based on the
					gradients.
				---------------------------------------------------"""
                batch_loss /= batch_size
                batch_weight_grads /= batch_size
                batch_biases_grads /= batch_size

                for i in range(len(self.layers)-1, 0, -1):
                    self.layers[i].weights -= lr * batch_weight_grads[i]
                    self.layers[i].biases -= lr * batch_biases_grads[i]

                losses.append(batch_loss.mean())

        return losses

    def predict(self, test_x):
        result = []

        for x in test_x:
            temp_x = x.copy()
            for k, l in enumerate(self.layers):
                temp_x = l.compute_layer(temp_x)

            result.append(temp_x)

        return np.asarray(result)

    def __str__(self):
        ret = "------------------------------------------------\n"
        for i, l in enumerate(self.layers):
            ret += "Layer: " + str(i) + " Size: " + str(l.num_nodes) + "\n"
        ret += "------------------------------------------------\n"
        return ret


if __name__ == "__main__":
    pass

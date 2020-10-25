import numpy as np


class MiniBatchGD(object):
    def __init__(self, layers, lr):
        super().__init__()
        self.lr = lr
        self.model_shape = [(l.weights.shape, l.biases.shape,)
                            for l in layers]

        self.weight_grads = np.asarray([np.zeros(x[0]) for x in self.model_shape])
        self.biases_grads = np.asarray([np.zeros(x[1]) for x in self.model_shape])
    
    def reset_gradients(self):
        self.weight_grads = np.asarray([np.zeros(x[0]) for x in self.model_shape])
        self.biases_grads = np.asarray([np.zeros(x[1]) for x in self.model_shape])

    def update_gradients(self, layers, error):
        for i in range(len(layers)-1, 0, -1):

            self.biases_grads[i] += error
            self.weight_grads[i] += np.multiply.outer(error, layers[i-1].output)

            # Calculating error for the layer below
            error = (layers[i].weights.T @ error) * \
                layers[i-1].activation.der(
                layers[i-1].weighted_sum)



    def step(self, layers, batch_size):

        self.weight_grads /= batch_size
        self.biases_grads /= batch_size

        for i in range(len(layers)-1, 0, -1):
            layers[i].weights -= self.lr * self.weight_grads[i]
            layers[i].biases -= self.lr * self.biases_grads[i]

class SGD(object):
    def __init__(self):
        super().__init__()

    def step(self):
        """
        * x_loss -> loss of the forward pass
        * x_err -> Error of the final layer
        """
        pass


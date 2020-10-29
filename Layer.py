import numpy as np
from Activations import ReLU, Sigmoid, Linear, Softmax

class Layer(object):
    def __init__(self):
        super().__init__()

class Dense(Layer):
    def __init__(self, num_nodes, input_shape, activation):
        super().__init__()
        self.prev_layer = None
        self.num_nodes = num_nodes
        self.input_shape = input_shape
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid(),
            'linear': Linear(),
            'softmax': Softmax()
        }[activation]

        # ************* He initialization ***************
        self.weights = np.random.randn(self.num_nodes, input_shape) * np.sqrt(2/input_shape)
        self.biases = np.zeros(shape=self.num_nodes)
        self.weighted_sum = np.empty(shape=self.num_nodes, dtype=float)
        self.output = []

        # DS's to hold the gradients while backprop
        self.weight_grads = np.zeros((self.num_nodes, self.input_shape))
        self.biases_grads = np.zeros(self.num_nodes)

    def reset_gradients(self):
        self.weight_grads = np.zeros((self.num_nodes, self.input_shape))
        self.biases_grads = np.zeros(shape=self.num_nodes)

    def update_gradients(self, error):
        if self.prev_layer is None:
            return

        self.biases_grads += error
        self.weight_grads += np.multiply.outer(error, self.prev_layer.output)

        curr_error = (self.weights.T @ error) * \
                self.prev_layer.activation.der(
                self.prev_layer.weighted_sum)

        return curr_error

    def backward(self, lr, batch_size):
        self.weight_grads /= batch_size
        self.biases_grads /= batch_size

        self.weights -= lr * self.weight_grads
        self.biases -= lr * self.biases_grads

    def compute_layer(self, input_data):
        self.weighted_sum = self.weights @ input_data + self.biases
        self.output = self.activation(self.weighted_sum)

        return self.output

    def __iter__(self):
        for node in zip(self.weights, self.biases):
            yield node

    def __str__(self):
        return f"NUM NODES: {self.num_nodes} ACTIVATON: {self.activation}" +\
            f"INPUT SHAPE: {self.input_shape}"

class Conv2D(Layer):
    """
    ********************** CHANNEL LAST ************************
    - Technically cross-correlation, as kernels are not flipped.
    """

    def __init__(self, filters, kernel_size, activation, input_shape, stride=(1, 1)):
        super().__init__()
        assert len(input_shape) == 3
        assert input_shape[2] <= 3

        self.filters = filters
        self.k = kernel_size

        if isinstance(stride, int):
            stride = (stride, stride)
        self.stride = stride

        self.depth = input_shape[2] # Channel last
        self.activation = {
            'relu': ReLU(),
            'sigmoid': Sigmoid(),
            'linear': Linear(),
            'softmax': Softmax()
        }[activation]
        self.prev_layer = None

        self.op_H = (input_shape[0] - self.k) // stride[0] + 1
        self.op_W = (input_shape[1] - self.k) // stride[1] + 1
        
        self.weighted_sum = np.zeros((self.op_H, self.op_W, filters))

        # Parameters to learn
        self.biases = np.zeros((self.op_H, self.op_W, filters))
        self.kernels = np.random.randn(filters, self.k, self.k, self.depth)

        self.output = None
        
        # DS's to store the gradients while backprop
        self.kernel_grads = np.zeros((filters, self.k, self.k, self.depth))
        self.biases_grads = np.zeros((self.op_H, self.op_W, filters))
        
    def compute_layer(self, input_data):
        self.input = input_data

        for f in range(self.filters):
            self.weighted_sum[:, :, f] = self.convolve(input_data, self.kernels[f], self.stride)

        self.weighted_sum += self.biases
        self.output = self.activation(self.weighted_sum)
        return self.output

    def reset_gradients(self):
        self.kernel_grads = np.zeros((filters, self.k, self.k))
        self.biases_grads = np.zeros((filters, self.op_H, self.op_W))

    def update_gradients(self, error):
        """
        Going to be insane
        """
        if self.prev_layer == None:
            return

    def convolve(self, input_data, kernel, stride=(1,1)):
   
        h_k = kernel.shape[0]
        w_k = kernel.shape[1]
        
        h = (input_data.shape[0] - h_k) // stride[0] + 1
        w = (input_data.shape[1] - w_k) // stride[1] + 1
    
        op = np.empty((h,w))
        for i in range(0, h, stride[0]):
            for j in range(0, w, stride[1]):
                slice_ = input_data[i:i+h_k, j:j+w_k]
                op[i, j] = np.sum(slice_ * kernel)
        
        return op

    def backward(self, lr, batch_size):
        self.kernel_grads /= batch_size
        self.biases_grads /= batch_size

        self.kernel_grads -= lr * self.kernel_grads
        self.biases -= lr * self.biases_grads

    def __call__(self, input_data):
        return self.compute_layer(input_data)

class Flatten(Layer):
    def __init__(self):
        super().__init__()
        self.prev_layer = None
        self.output = None
        self.weighted_sum = None

    def compute_layer(self, input_data):
        self.output = np.asarray(input_data).flatten()
        self.weighted_sum = self.output
        return self.output

class MaxPool2D(Layer):
    def __init__(self, kernel_size):
        super().__init__()
        self.k = kernel_size
        self.prev_layer = None
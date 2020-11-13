import numpy as np
from .Activations import ReLU, Sigmoid, Linear, Softmax

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

    def __call__(self, x):
        return self.compute_layer(x)

class Conv2D(Layer):
    """
    ********************** CHANNEL LAST ************************
    """

    def __init__(self, filters, kernel_size, activation, input_shape=None, stride=(1, 1)):
        super().__init__()
        
        self.input_shape = input_shape
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
        self.biases = np.zeros((self.op_H, self.op_W, self.filters))
        self.kernels = np.random.randn(self.k, self.k, self.depth, self.filters)

        self.output = None
        
        # DS's to store the gradients while backprop
        self.kernel_grads = np.zeros((self.k, self.k, self.depth, self.filters))
        self.biases_grads = np.zeros((self.op_H, self.op_W, self.filters))
        
    def convolve(self, input_data, kernel, stride=(1,1), mode="normal"):
        
        assert len(input_data.shape) == len(kernel.shape)

        h_k = kernel.shape[0]
        w_k = kernel.shape[1]
        
        h_i = input_data.shape[0]
        w_i = input_data.shape[1]
        
        if mode == 'full':
            h = (h_i + h_k) // stride[0] - 1
            w = (w_i + w_k) // stride[1] - 1
            pad_h = (max(h_i-h_k, 1),max(h_i-h_k, 1))
            pad_w = (max(w_i-w_k, 1),max(w_i-w_k, 1))
            ip = np.pad(input_data, (pad_h, pad_w, (0,0)))
        else:
            h = (h_i - h_k) // stride[0] + 1
            w = (w_i - w_k) // stride[1] + 1
            ip = input_data

        if len(kernel.shape) == 2:
            notation = "HWhw,hw->HW"
            shape_ = (h,w,h_k,w_k)
            strides_ = (
                ip.strides[0],
                ip.strides[1],
                ip.strides[0],  
                ip.strides[1]
            )
        elif len(kernel.shape) == 3:
            notation = "HWhwd,hwd->HW"
            shape_ = (h,w,h_k,w_k,kernel.shape[2])
            strides_ = (
                ip.strides[0],
                ip.strides[1],
                ip.strides[0],  
                ip.strides[1],
                ip.strides[2]
            )

        expanded_input = np.lib.stride_tricks.as_strided(
            ip,
            shape=shape_,
            strides=strides_,
            writeable=False)

        op = np.einsum(
                notation,
                expanded_input,
                kernel)

        return op

    def compute_layer(self, input_data):
        for f in range(self.filters):
            self.weighted_sum[:, :, f] = self.convolve(input_data, 
                                            self.kernels[:, :, :, f],
                                            self.stride)

        self.weighted_sum += self.biases
        self.output = self.activation(self.weighted_sum)
        return self.output

    def reset_gradients(self):
        self.kernel_grads = np.zeros((self.k, self.k, self.depth, self.filters))
        self.biases_grads = np.zeros((self.op_H, self.op_W, self.filters))

    def update_gradients(self, error):
 
        if self.prev_layer == None:
            return

        # ************************* LOOKS UGLY : TRY REFACTORING IT *************************
        for f in range(self.filters):
            for d in range(self.depth):
                self.kernel_grads[:,:,d,f] += self.convolve(self.prev_layer.output[:,:,d],
                                             error[:,:,f])
        # ***********************************************************************************
        curr_error = np.empty(self.prev_layer.output.shape)
        reshaped_kernels = self.kernels.reshape(self.k, self.k, self.filters, self.depth)

        for d in range(self.depth):
            curr_error[:,:,d] = self.convolve(error, reshaped_kernels[:,:,:,d], mode='full') 
            
        curr_error = curr_error * self.prev_layer.activation.der(
                                    self.prev_layer.weighted_sum)

        return curr_error

    def backward(self, lr, batch_size):
        self.kernel_grads /= batch_size
        self.biases_grads /= batch_size

        self.kernels -= lr * self.kernel_grads
        self.biases -= lr * self.biases_grads

    def __call__(self, input_data):
        return self.compute_layer(input_data)

class MaxPool2D(Layer):
    def __init__(self, kernel_size, input_shape):
        super().__init__()
        self.k = kernel_size
        self.prev_layer = None
        self.stride = (self.k, self.k)

        self.op_H = (input_shape[0] - self.k) // self.stride[0] + 1
        self.op_W = (input_shape[1] - self.k) // self.stride[1] + 1

        self.depth = input_shape[2] # channel last

    def compute_layer(self, input_data):
        kernel_size = (self.k, self.k, self.depth)
        A_w = np.lib.stride_tricks.as_strided(input_data, 
                shape=(self.op_H , self.op_W) + kernel_size, 
                strides=(self.stride[0]*input_data.strides[0],
                            self.stride[1]*input_data.strides[1]) + input_data.strides)
        A_w = A_w.reshape(-1, *kernel_size)
        print(A_w)

        return A_w.max(axis=(1,2)).reshape((self.op_H, self.op_W, self.depth))


    def reset_gradients(self):
        pass

    def update_gradients(self, error):
        return error.reshape(self.prev_layer.output.shape)
    
    def backward(self, lr, batch_size):
        pass

    def __call__(self, x):
        return self.compute_layer(x)

class Flatten(Layer):
    def __init__(self, input_shape=None):
        super().__init__()
        self.input_shape = None
        self.prev_layer = None
        self.output = None
        self.weighted_sum = None
        self.activation = Linear()

    def compute_layer(self, input_data):
        self.output = np.asarray(input_data).flatten()
        self.weighted_sum = self.output
        return self.output

    def reset_gradients(self):
        pass

    def update_gradients(self, error):
        return error.reshape(self.prev_layer.output.shape)
    
    def backward(self, lr, batch_size):
        pass
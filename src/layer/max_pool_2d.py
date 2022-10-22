import numpy as np

from layer import Layer


class MaxPool2D(Layer):
    def __init__(self, kernel_size, input_shape):
        super().__init__()
        self.k = kernel_size
        self.prev_layer = None
        self.stride = (self.k, self.k)

        self.op_H = (input_shape[0] - self.k) // self.stride[0] + 1
        self.op_W = (input_shape[1] - self.k) // self.stride[1] + 1

        self.depth = input_shape[2]  # channel last

    def compute_layer(self, input_data):
        kernel_size = (self.k, self.k, self.depth)
        A_w = np.lib.stride_tricks.as_strided(input_data,
                                              shape=(self.op_H, self.op_W) + kernel_size,
                                              strides=(self.stride[0] * input_data.strides[0],
                                                       self.stride[1] * input_data.strides[1]) + input_data.strides)
        A_w = A_w.reshape(-1, *kernel_size)
        print(A_w)

        return A_w.max(axis=(1, 2)).reshape((self.op_H, self.op_W, self.depth))

    def reset_gradients(self):
        pass

    def update_gradients(self, error):
        return error.reshape(self.prev_layer.output.shape)

    def backward(self, lr, batch_size):
        pass

    def __call__(self, x):
        return self.compute_layer(x)

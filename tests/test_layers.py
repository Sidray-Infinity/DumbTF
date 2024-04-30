import unittest

import numpy as np

from dumbtf.layer.conv_2d import Conv2D
from dumbtf.layer.dense import Dense


class TestLayers(unittest.TestCase):
    def test_dense_forward(self):
        x = np.random.randn(789)
        x = Dense(10, input_shape=789, activation='relu')(x)

        self.assertEqual(x.shape, (10,))

    def test_conv2d_forward(self):
        x = np.random.randn(28, 28, 1)
        x = Conv2D(32, input_shape=(28, 28, 1), kernel_size=3, activation='relu')(x)

        self.assertEqual(x.shape, (26, 26, 32))


if __name__ == "__main__":
    unittest.main()

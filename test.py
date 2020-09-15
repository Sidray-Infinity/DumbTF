
import numpy as np

def func(a):
    a[0][0] = 1

if __name__ == "__main__":
    a = np.zeros((2,2))
    func(a)
    print(a)


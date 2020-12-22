"""
    straw hat function
"""
import numpy as np

class StrawHat(object):
    def __call__(self, x):
        x1 = x[0]
        x2 = x[1]
        r = np.sqrt(np.square(x1)+np.square(x2))
        return np.true_divide(np.sin(r),r+0.0001)
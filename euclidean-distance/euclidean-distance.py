import numpy as np

def euclidean_distance(x, y):
    kqua = 0
    if len(x) != len(y):
        raise ValueError('must have the same')
    else:
        for i in range(len(x)):
            kqua += (x[i]-y[i])**2
        return np.sqrt(kqua)
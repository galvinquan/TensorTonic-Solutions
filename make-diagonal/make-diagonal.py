import numpy as np

def make_diagonal(v):
    ma = np.zeros((len(v),len(v)))
    for i in range(len(v)):
        ma[i][i] = v[i]
    return ma
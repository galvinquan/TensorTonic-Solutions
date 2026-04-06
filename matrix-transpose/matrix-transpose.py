import numpy as np

def matrix_transpose(A):
    ma = np.zeros((len(A[0]),len(A)))
    for i in range(len(A)):
        for j in range(len(A[0])):
            ma[j][i] = A[i][j]
    return ma
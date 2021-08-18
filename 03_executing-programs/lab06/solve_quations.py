import numpy as np
from itertools import combinations,permutations


def pivot(M,i):
    return M[i] / M[i,i] # first row divided by A[0,0]


def rowOperation(M,i,j):
    return -M[j,i]*M[i] + M[j]

def Gaussian(M):
    for i,j in combinations(range(len(M)),2):
        if M[i,i] != 1:
            M[i] = pivot(M,i) # first row divided by A[0,0] pivot
        M[j] = rowOperation(M,i,j) # row operation
    M[len(M)-1] = pivot(M,len(M)-1)
    return M

def GaussJordan(M):
    for i,j in permutations(range(len(M)),2):
        if M[i,i] != 1: # pivot
            M[i] = pivot(M,i) # first row divided by A[0,0] pivot
        M[j] = rowOperation(M,i,j) # row operation
    return M

if __name__ == "__main__":
    A = np.array([[2,4,6,18],[4,5,6,24],[3,1,-2,4]])
    B = np.array([[1,-2,-3,0],[-1,1,2,3],[0,2,1,-8]],dtype=float)
    print(A)
    print()
    A2 = Gaussian(A)
    print(A2)
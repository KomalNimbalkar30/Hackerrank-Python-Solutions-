import numpy as np
N,m=map(int,input().split())

A = np.array([input().split() for _ in range(N)],int)

print(np.prod(np.sum(A, axis=0),axis=0))

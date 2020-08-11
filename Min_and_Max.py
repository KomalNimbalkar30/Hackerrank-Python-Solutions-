import numpy as np
N,M=map(int,input().split())

A = np.array([input().split() for _ in range(N)],int)


np.set_printoptions(legacy='1.13')

print(np.mean(A, axis=1), np.var(A,axis=0), np.std(A), sep="\n")






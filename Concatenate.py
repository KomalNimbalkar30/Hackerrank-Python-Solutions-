import numpy as np

n,m,p=map(int,input().split())
A = np.array([input().split() for _ in range(n)],int)
B = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((A,B),axis=0))

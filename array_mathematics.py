import numpy as np

N,m=map(int,input().split())

a, b = (np.array([input().split() for _ in range(N)],dtype=int) for _ in range(2))

print(a+b, a-b, a*b, a//b, a%b, a**b, sep="\n")
    


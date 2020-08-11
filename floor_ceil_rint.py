import numpy as np

arr=np.array(list(map(float,input().split())))

fl=np.floor(arr)
ce=np.ceil(arr)
ri=np.rint(arr)

np.set_printoptions(sign=' ')

print(fl,ce,ri,sep='\n')


import numpy

def arrays(arr):
    arr=numpy.array(arr)
    return(arr.sort())

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

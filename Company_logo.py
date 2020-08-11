import numpy

def arrays(arr):
    return(numpy.array(arr[::-1], float))


arr = input().strip().split(' ')


'''
import numpy

def arrays(arr):
    arr=numpy.array(arr)
    arr2=numpy.sort(arr)
    return(arr2)


arr = list(map(float,input().strip().split(' ')))
result = arrays(arr)
print(result)

'''

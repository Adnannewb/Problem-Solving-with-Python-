import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result=numpy.array(arr,float)
    return numpy.flip(result)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
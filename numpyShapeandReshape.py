import numpy

def arrays(arr):
    result=numpy.array(arr,int)
    return numpy.reshape(result,(3,3))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
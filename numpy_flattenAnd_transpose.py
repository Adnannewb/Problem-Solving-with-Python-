import numpy 
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

array = numpy.array(matrix)
print(numpy.transpose(array))
print(array.flatten())
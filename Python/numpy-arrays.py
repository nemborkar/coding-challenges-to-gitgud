import numpy

def arrays(arr):
    arr.reverse()
    np_array = numpy.array(arr, dtype=float)
    return np_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
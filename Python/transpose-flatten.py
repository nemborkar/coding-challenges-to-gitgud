# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

n, m = input().split()
n = int(n) # 0 axis
m = int(m) # 1 axis

first_array = numpy.zeros((n,m), dtype=int)

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

print(numpy.transpose(first_array))
print(first_array.flatten())
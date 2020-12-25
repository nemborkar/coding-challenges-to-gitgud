# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n = int(input()) # 0 axis

first_array = numpy.empty((n,n), dtype=int)
second_array = numpy.empty((n,n), dtype=int)

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        second_array[i,j] = int(input_string[j])

# inputs are working
# ----------------------------------------------

print(numpy.dot(first_array,second_array))

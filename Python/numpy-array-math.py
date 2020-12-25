# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

n, m = input().split()
n = int(n)
m = int(m)

first_array = numpy.zeros((n,m), dtype=int)
second_array = numpy.zeros((n,m), dtype=int)

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        second_array[i,j] = int(input_string[j])

print(numpy.add(first_array,second_array))
print(numpy.subtract(first_array,second_array))
print(numpy.multiply(first_array,second_array))
print(numpy.floor_divide(first_array,second_array))
print(numpy.mod(first_array,second_array))
print(numpy.power(first_array,second_array))
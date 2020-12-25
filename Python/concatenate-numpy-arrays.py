# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

n, m, p = input().split()
n = int(n)
m = int(m)
p = int(p)

first_array = numpy.zeros((n,p), dtype=int)
second_array = numpy.zeros((m,p), dtype=int)

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

for i in range(m):
    input_string = input().split()
    for j in range(len(input_string)):
        second_array[i,j] = int(input_string[j])

print(numpy.concatenate((first_array,second_array),axis=0))
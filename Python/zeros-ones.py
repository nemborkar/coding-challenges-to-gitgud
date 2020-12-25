# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy
import sys

input_string = input().split()

for i in range(len(input_string)):
    input_string[i] = int(input_string[i])
    if input_string[i] < 1 or input_string[i] > 3:
        sys.exit()

print(numpy.zeros(input_string, dtype=numpy.int))
print(numpy.ones(input_string, dtype=numpy.int))
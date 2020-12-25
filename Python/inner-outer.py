# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

first_string = input().split()
second_string = input().split()

for i in range(len(first_string)):
    first_string[i] = int(first_string[i])

for i in range(len(second_string)):
    second_string[i] = int(second_string[i])

first_array = numpy.array(first_string)
second_array = numpy.array(second_string)

print(numpy.inner(first_array,second_array))
print(numpy.outer(first_array,second_array))
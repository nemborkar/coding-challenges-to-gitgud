# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(input().split())
A = numpy.float64(A)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = input().split()
n = int(n)
m = int(m)

np_matrix = numpy.eye(n,m, k=0)

print(np_matrix)
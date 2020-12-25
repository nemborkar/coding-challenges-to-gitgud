# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

p_coeff = input().split()
x = float(input())

for i in range(len(p_coeff)):
    p_coeff[i] = float(p_coeff[i])

print(numpy.polyval(p_coeff,x))
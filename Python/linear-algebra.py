# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

n = int(input())

first_array = numpy.empty((n,n), dtype=float)

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = float(input_string[j])

final_answer = round(numpy.linalg.det(first_array), 2)

print(final_answer)
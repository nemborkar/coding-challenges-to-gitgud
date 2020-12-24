# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# had to round standard deviation to 11 digits after decimal because
# that's what the expected output was requesting


import numpy

n, m = input().split()
n = int(n) # 0 axis
m = int(m) # 1 axis

first_array = numpy.zeros((n,m))

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

z = numpy.std(first_array, axis=None)

print(numpy.mean(first_array, axis=1))
print(numpy.var(first_array, axis=0))
print(round(z,11))
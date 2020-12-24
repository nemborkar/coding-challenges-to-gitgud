# https://www.hackerrank.com/challenges/np-min-and-max/problem
# after understanding numpy and figuring out the input process,
# this one was too easy

import numpy

# this chunk is working and enable it later
n, m = input().split()
n = int(n) # 0 axis
m = int(m) # 1 axis

first_array = numpy.zeros((n,m))

for i in range(n):
    input_string = input().split()
    for j in range(len(input_string)):
        first_array[i,j] = int(input_string[j])

my_final_array = numpy.min(first_array, axis=1)

print(int(numpy.max(my_final_array)))






# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# for this one, the output itself is pretty easy to show
# getting the right input is the real challenge here
# numpy was the hint; took a quick tutorial and
# used it in tandem with string split into array

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

my_final_array = numpy.sum(first_array, axis=0)

print(int(numpy.product(my_final_array)))



# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy
import sys

string_list = input().split()

if len(string_list)>9:
    sys.exit()

np_array = numpy.array(string_list, dtype=int)
print(numpy.reshape(np_array,(3,3)))
# !/bin/python3

import math
import os
import random
import re
import sys


def avg(a):
    float_answer = sum(a)/len(a)
    float_answer = round(float_answer, 2)
    return float_answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    if len(nums) < 1 or len(nums) > 100:
        sys.exit()

    for i in range(len(nums)):
        if nums[i] < -100 or nums[i] > 100:
            sys.exit()

    res = avg(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()
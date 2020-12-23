# https://www.hackerrank.com/challenges/write-a-function/problem
# % (mod) implies evenly divisble

import sys

def is_leap(year):
    leap = False

    # Write your logic here
    if year < 1900 or year > 10 ** 5:
        sys.exit()

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap

year = int(input())
print(is_leap(year))
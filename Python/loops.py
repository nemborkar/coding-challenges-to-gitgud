# https://www.hackerrank.com/challenges/python-loops/problem

import sys

if __name__ == '__main__':
    n = int(input())

    if n < 1 or n > 20:
        sys.exit()

    i = 0
    while i < n:
        print(i*i)
        i += 1
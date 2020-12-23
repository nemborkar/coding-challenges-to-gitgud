# https://www.hackerrank.com/challenges/python-print/problem
# print( * , end="") can be used to print on the same line with no spaces


import sys

if __name__ == '__main__':
    n = int(input())

    if n < 1 or n > 150:
        sys.exit()

    a = []
    for i in range(n):
        a.append(i+1)
        print(a[i], end="")

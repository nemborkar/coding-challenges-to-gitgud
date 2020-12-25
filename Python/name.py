# https://www.hackerrank.com/challenges/whats-your-name

import sys

def print_full_name(a, b):
    if len(a) > 10 or len(b) > 10:
        sys.exit()
    c = a + " " + b + "!"
    print("Hello",c, "You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

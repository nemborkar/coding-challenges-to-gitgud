# https://www.hackerrank.com/challenges/python-mutations/problem
# since string are immutable in python, we might have to split and join
# nope... guess we just have to do it with brute force


def mutate_string(string, position, character):

    new_string = string[:position]
    new_string = new_string + character
    second_half = string[position+1:]
    return new_string + second_half

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

import sys

if __name__ == '__main__':
    n = int(input())

    if n < 2 or n > 10:
        sys.exit()

    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        if scores[i] > 100 or scores[i] < 0 or len(scores) < 3 or len(scores) > 3:
            sys.exit()
        student_marks[name] = scores

    query_name = input()
    final_list = student_marks[query_name]
    unformatted_answer = (final_list[0] + final_list[1] + final_list[2]) / 3
    final_answer = format(unformatted_answer, '.2f')
    print(final_answer)
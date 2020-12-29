
import sys

def avg(a):
    float_answer = sum(a)/len(a)
    float_answer = round(float_answer, 2)
    return float_answer


input_string = input().split()
if len(input_string) < 1 or len(input_string) > 100:
    sys.exit()

for i in range(len(input_string)):
    input_string[i] = int(input_string[i])
    if input_string[i] < -100 or input_string[i] > 100:
        sys.exit()

print(avg(input_string))
# https://www.hackerrank.com/challenges/the-minion-game/problem
# Input one string
# make all possible substrings
# count substrings
# if starts with vowel, Kevin gets point
# if starts with consonant, Stuart gets point
# give scores to the substrings

def minion_game(S):
    # your code goes here
    S = str(S.upper())

    final_list = []
    Kevin = []
    Stuart = []

    for m in range(0, len(S)):
        for n in range(1, len(S) + 1):
            if m >= n:
                continue
            else:
                final_list.append(S[m:n])

    for w in final_list:
        #print(w[0])
        if w[0] in ('A', 'E', 'I', 'O', 'U'):
            Kevin.append(w)
        else:
            Stuart.append(w)

    if len(Kevin) > len(Stuart):
        print("Kevin", len(Kevin))
    elif len(Kevin) < len(Stuart):
        print("Stuart", len(Stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
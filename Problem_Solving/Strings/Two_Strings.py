#!/bin/python3

import os

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    verifiedChars = {letter: False for letter in 'qwertyuiopasdfghjklzxcvbnm'}

    for c in s1:
        if not verifiedChars[c]:
            verifiedChars[c] = True
            if c in s2:
                return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

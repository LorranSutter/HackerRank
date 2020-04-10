#!/bin/python3

import os

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            deletions += 1
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

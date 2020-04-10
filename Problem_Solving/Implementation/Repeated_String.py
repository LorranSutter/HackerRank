#!/bin/python3

import os

# Complete the repeatedString function below.


def repeatedString(s, n):
    countAs = s.count('a')
    countS = n // len(s)
    remainSub = n % len(s)
    countASub = s[:remainSub].count('a')

    return countS*countAs + countASub


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

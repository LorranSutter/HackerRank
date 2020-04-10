#!/bin/python3

import os

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    numJumps, i = 0, 0
    lenC = len(c)
    while i < lenC-1:
        print(i, c[i])
        if i+2 < lenC and c[i+2] != 1:
            i += 1
        numJumps += 1
        i += 1
    return numJumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

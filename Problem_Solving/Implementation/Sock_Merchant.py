#!/bin/python3

import os

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    pairDict = dict()
    for sock in ar:
        if sock not in pairDict.keys():
            pairDict[sock] = 0
        pairDict[sock] += 1

    matches = 0
    for i in pairDict.values():
        matches += i//2

    return matches


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import os

# Complete the maximumToys function below.


def maximumToys(prices, k):
    tot = 0
    num = 0
    for p in sorted(prices):
        tot += p
        if tot > k:
            break
        num += 1
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

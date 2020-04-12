#!/bin/python3

import os
from math import inf

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr, n):
    res = 0
    if n == len(set(arr)):
        arr.sort()
        res = inf
        for i in range(n-1):
            newAbs = abs(arr[i] - arr[i+1])
            if newAbs == 1:
                res = 1
                break
            if newAbs < res:
                res = newAbs

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()

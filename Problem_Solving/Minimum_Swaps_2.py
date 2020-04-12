#!/bin/python3

import os

# Complete the minimumSwaps function below.


def minimumSwaps(arr, n):
    arr = list(map(lambda x: int(x)-1, arr))

    swaps = 0
    for i in range(n):
        while True:
            if arr[i] == i:
                break
            pos2 = arr[i]
            arr[i], arr[pos2] = arr[pos2], arr[i]
            swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()

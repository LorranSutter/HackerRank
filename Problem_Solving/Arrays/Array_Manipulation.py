#!/bin/python3

import os

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    arr = [0] * (n+1)

    for query in queries:
        a, b, k = query

        arr[a-1] += k
        if b <= n:
            arr[b] -= k

    maxValue = a = 0
    for i in arr:
        a += i
        if maxValue < a:
            maxValue = a

    return maxValue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

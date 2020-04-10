#!/bin/python3

import math
import os


def printHourGlass(arr, initCornerPos):
    i, j = initCornerPos[0], initCornerPos[1]
    print('{} {} {}'.format(arr[i][j], arr[i][j+1], arr[i][j+2]))
    print('  {}   '.format(arr[i+1][j+1]))
    print('{} {} {}'.format(arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]))

# Complete the hourglassSum function below.


def hourglassSum(arr, n):
    maxS = -math.inf
    for i in range(n-2):
        for j in range(n-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if s > maxS:
                maxS = s
    return maxS


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr, 6)

    fptr.write(str(result) + '\n')

    fptr.close()

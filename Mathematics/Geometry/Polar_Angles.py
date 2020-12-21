#!/bin/python3

import os
import sys
import math

# Complete the solve function below.


def solve(coordinates):
    return sorted(coordinates, key=lambda x: (math.atan2(x[1], x[0]) % (2*math.pi), x[0]**2 + x[1]**2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

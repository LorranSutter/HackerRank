#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    if r%2 == 0:
        return 5*(r-2) + c*2-1
    return 5*(r-1) + c*2-2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()

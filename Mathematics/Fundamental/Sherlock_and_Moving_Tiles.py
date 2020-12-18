#!/bin/python3

import os
import sys
from math import sqrt

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    allResults = []
    for query in queries:
        res1 = -(sqrt(2)*l*(s1-s2) + sqrt(2)*sqrt(query)*(s1-s2))/((s1-s2)**2)
        res2 = -(sqrt(2)*l*(s1-s2) - sqrt(2)*sqrt(query)*(s1-s2))/((s1-s2)**2)
        
        if res1 < res2 and res1 >= 0:
            allResults.append(abs(res1))
        else:
            allResults.append(abs(res2))
    return allResults

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

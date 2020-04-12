#!/bin/python3

import os

# Complete the luckBalance function below.


def luckBalance(k, contests):
    luckBalance = 0
    importantContests = []
    for contest in contests:
        L, T = contest

        if T == 0:
            luckBalance += int(L)
        else:
            importantContests.append(int(L))

    importantContests.sort()

    if k == 0:
        luckBalance -= sum(importantContests)
    else:
        luckBalance += sum(importantContests[-k:]) - \
            sum(importantContests[:-k])

    return luckBalance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

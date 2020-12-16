#!/bin/python3

import math


def divisors(n):
    div = [1, n]
    for k in range(2, n//2+1):
        if n % k == 0:
            div.append(k)
    return div


def bestDivisor(div):
    best = 1
    bestSum = 0
    for num in div:
        s = 0
        digit = num
        while digit >= 10:
            s += digit % 10
            digit //= 10
        s += digit
        if s >= bestSum:
            if s > bestSum:
                best = num
                bestSum = s
            elif num < best:
                best = num
                bestSum = s

    return best


if __name__ == '__main__':
    n = int(input())
    div = divisors(n)
    print(bestDivisor(div))

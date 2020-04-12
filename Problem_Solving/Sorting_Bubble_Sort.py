#!/bin/python3

# Complete the countSwaps function below.


def countSwaps(a, n):
    numSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1

    print('Array is sorted in {} swaps.'.format(numSwaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)

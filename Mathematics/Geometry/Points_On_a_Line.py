#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    horizontal = [points[k][0] == points[k+1][0] for k in range(n-1)]
    vertical = [points[k][1] == points[k+1][1] for k in range(n-1)]

    if all(horizontal) or all(vertical):
        print('YES')
    else:
        print('NO')

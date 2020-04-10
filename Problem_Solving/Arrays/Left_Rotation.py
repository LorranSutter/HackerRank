#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    d = d % n

    if d == 0:
        res = ''
        for elem in a:
            res += str(elem) + ' '

        print(res[:-1])
    else:
        res = [0 for k in range(n)]

        for i in range(n):
            newPosition = i-d

            if newPosition < 0:
                res[newPosition+n] = str(a[i])
            else:
                res[newPosition] = str(a[i])

        print(' '.join(res))

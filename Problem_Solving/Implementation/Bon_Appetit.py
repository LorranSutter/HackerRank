#!/bin/python3

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    bill.pop(k)

    charge = b - sum(bill)//2

    print('Bon Appetit' if charge == 0 else charge)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

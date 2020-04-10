# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

X = input()
shoes = collections.Counter(input().split())

res = 0
for k in range(int(input())):
    size, value = input().split()

    if shoes[size] > 0:
        shoes[size] -= 1
        res += int(value)

print(res)

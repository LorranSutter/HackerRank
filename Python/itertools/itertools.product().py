# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

l = [str(p) for p in itertools.product(A, B)]
print(" ".join(l))

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

S, K = input().split()

for k in range(1, int(K)+1):
    comb = [sorted(c) for c in itertools.combinations(S, k)]
    for c in sorted(comb):
        print("".join(c))

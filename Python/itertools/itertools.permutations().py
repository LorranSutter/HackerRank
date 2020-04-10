# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

S, K = input().split()

for k in sorted(itertools.permutations(S, int(K))):
    print("".join(k))

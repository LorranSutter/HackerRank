from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for k in range(1, n+1):
    d[input()].append(str(k))

for _ in range(m):
    output = ' '.join(d[input()])
    print(-1 if output == '' else output)

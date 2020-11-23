import numpy

N, M, P = list(map(int,input().split()))

arrays = [list(map(int,input().split())) for _ in range(N+M)]

print(numpy.concatenate([arrays]))

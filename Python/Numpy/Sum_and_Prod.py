import numpy

N = int(input().split()[0])

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

A = numpy.array(A)
S = numpy.sum(A, axis=0)

print(numpy.prod(S, axis=None))

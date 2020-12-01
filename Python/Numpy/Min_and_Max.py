import numpy

N = int(input().split()[0])

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

A = numpy.array(A)

print(numpy.max(numpy.min(A, axis=1), axis=None))

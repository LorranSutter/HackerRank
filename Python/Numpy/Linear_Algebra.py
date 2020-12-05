import numpy

N = int(input())

A = []
for _ in range(N):
    A.append(list(map(float, input().split())))

A = numpy.array(A)

print(numpy.round(numpy.linalg.det(A), 2))

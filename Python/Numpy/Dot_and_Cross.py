import numpy

N = int(input().split()[0])

A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

A = numpy.array(A)
B = numpy.array(B)

print(numpy.dot(A, B))

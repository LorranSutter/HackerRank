import numpy

N = int(input().split()[0])

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

A = numpy.array(A)

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A), 11))

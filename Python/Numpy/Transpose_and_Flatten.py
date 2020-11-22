import numpy

N, M = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

mat = numpy.array(mat)

print(numpy.transpose(mat))
print(mat.flatten())

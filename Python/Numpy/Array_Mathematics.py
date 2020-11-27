import numpy

N, M = tuple(map(int, input().split()))
A, B = [], []

for _ in range(N):
    A.append(list(map(int, input().split())))
A = numpy.array(A)

for _ in range(N):
    B.append(list(map(int, input().split())))
B = numpy.array(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A % B)
print(A**B)

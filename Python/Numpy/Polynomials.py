import numpy

P = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(P, x))

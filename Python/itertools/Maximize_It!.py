from itertools import product

K, M = map(int, input().split())

arrays = []

for _ in range(K):
    array = list(map(int, input().split()))[1:]
    arrays.append(array)

maxComb = 0
for combinations in product(*arrays):
    combinationSum = sum(map(lambda x: x*x, combinations)) % M

    if combinationSum > maxComb:
        maxComb = combinationSum

print(maxComb)

from math import inf
from collections import deque

for _ in range(int(input())):
    input()
    cubes = deque(map(int, input().split()))

    currentCube = inf
    while len(cubes) > 0:
        maxCube = max(cubes[0], cubes[-1])
        if currentCube >= maxCube:
            if maxCube == cubes[0]:
                currentCube = cubes[0]
                cubes.popleft()
            else:
                currentCube = cubes[-1]
                cubes.pop()
        else:
            break
    print('Yes' if len(cubes) == 0 else 'No')

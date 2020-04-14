# One test case seems to be wrong. It says that the result should be 3, but it is obviously 1

#!/bin/python3

import os
from collections import Counter

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    arr = Counter(arr)
    return arr.most_common()[0][0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

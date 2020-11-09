#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()
    count = Counter([letter for letter in s])

    sortedCount = sorted(count.items(), key=lambda item: (-item[1], item[0]))

    for item in sortedCount[:3]:
        print(*item)

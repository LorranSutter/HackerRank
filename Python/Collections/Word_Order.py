from collections import OrderedDict

d = OrderedDict()

for _ in range(int(input())):
    word = input()
    if word not in d.keys():
        d[word] = 1
    else:
        d[word] += 1

print(len(d))
print(*d.values())

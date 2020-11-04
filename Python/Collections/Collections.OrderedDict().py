from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item = input().split()
    qty = int(item[-1])
    item = ' '.join(item[:-1])

    if item in d.keys():
        d[item] += qty
    else:
        d[item] = qty

for item, qty in d.items():
    print('{} {}'.format(item, qty))

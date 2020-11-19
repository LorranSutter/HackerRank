import itertools

frequencies = []
for key, group in itertools.groupby(input()):
    frequencies.append((len(list(group)), int(key)))

print(*frequencies)

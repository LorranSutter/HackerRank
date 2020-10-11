import re

regExp = r':?.(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})'
for _ in range(int(input())):
    matches = re.findall(regExp, input())

    for match in matches:
        print(match)

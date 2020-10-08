import re

regExp = r'^[987]{1}\d{9}$'

for _ in range(int(input())):
    print('NO' if re.search(regExp, input()) is None else 'YES')

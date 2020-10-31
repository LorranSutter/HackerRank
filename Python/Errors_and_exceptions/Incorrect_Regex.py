import re

for _ in range(int(input())):
    try:
        re.match(input(), '')
        print('True')
    except:
        print('False')

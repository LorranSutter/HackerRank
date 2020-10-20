import re

for _ in range(int(input())):
    output = re.sub("(?<= )&&(?= )", "and", input())
    print(re.sub("(?<= )\|\|(?= )", "or", output))

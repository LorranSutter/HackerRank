import re
import email.utils

regExp = r'^[A-Za-z][\w\-_\.]+@[A-Za-z]+\.[A-Za-z]{1,3}$'

for _ in range(int(input())):
    inputData = email.utils.parseaddr(input())
    if(re.match(regExp, inputData[1])):
        print(email.utils.formataddr(inputData))

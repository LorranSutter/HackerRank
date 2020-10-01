def fun(s):
    # return True if s is a valid email, else return False

    s = s.split('@')

    if(len(s) != 2):
        return False

    s = [s[0]] + s[1].split('.')
    if(len(s) != 3):
        return False

    lettersNums = 'abcdefghijklmnopqrstuvwxyz0123456789'
    usernameChars = lettersNums + '-_'

    if(len(s[0]) == 0 or len(s[1]) == 0 or len(s[2]) > 3):
        return False
    if(any([char.lower() not in usernameChars for char in s[0]])):
        return False
    if(any([char.lower() not in lettersNums for char in s[1]])):
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

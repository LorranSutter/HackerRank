def count_substring(string, sub_string):
    lenS1 = len(string)
    lenS2 = len(sub_string)

    ans = 0
    for i in range(lenS1-lenS2+1):
        if string[i:i+lenS2] == sub_string:
            ans += 1

    return ans


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

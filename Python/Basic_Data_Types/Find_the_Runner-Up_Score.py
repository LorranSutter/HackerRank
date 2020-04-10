if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    for k in arr:
        if k != arr[0]:
            print(k)
            break

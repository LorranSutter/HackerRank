if __name__ == '__main__':
    n = int(input())
    integer_tuple = tuple(map(int, input().split()))
    print(integer_tuple.__hash__())

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    A = set(map(int, input().split()))
    superset = True

    for N in range(int(input())):
        B = set(map(int, input().split()))

        if not B < A:
            superset = False
            break

    print(superset)

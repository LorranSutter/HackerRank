# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
arr = tuple(input().split())
A = set(input().split())
B = set(input().split())

tot = 0
for elem in arr:
    if elem in A:
        tot += 1
    elif elem in B:
        tot -= 1

print(tot)

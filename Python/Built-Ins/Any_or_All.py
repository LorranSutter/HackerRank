# Enter your code here. Read input from STDIN. Print output to STDOUT

N = input()
S = input().split()

print(all(int(s) > 0 for s in S) and any(s == s[::-1] for s in S))

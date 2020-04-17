n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    task = input().split()

    if task[0] == 'pop':
        s.pop()
    elif task[0] == 'remove':
        s.remove(int(task[1]))
    else:
        s.discard(int(task[1]))

print(sum(s))

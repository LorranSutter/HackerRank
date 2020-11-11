N, M = map(int, input().split())

for k in range(N//2):
    hifens = (M - 3*(2*k+1))//2
    print('{0}{1}{0}'.format(hifens*'-', (2*k+1)*'.|.'))

hifens = (M-7)//2
print('{0}{1}{0}'.format(hifens*'-', 'WELCOME'))

for k in range(N//2-1, -1, -1):
    hifens = (M - 3*(2*k+1))//2
    print('{0}{1}{0}'.format(hifens*'-', (2*k+1)*'.|.'))

def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    maxLength = size*4 - 3  # size*2-1 + size*2-2 letters and hyphens

    for k in range(size):
        alpha = alphabet[size-k-1:size]
        letters = '-'.join(alpha[::-1] + alpha[1:])
        hyphens = (maxLength - len(letters))//2
        print('-'*hyphens + letters + '-'*hyphens)

    for k in range(size-2, -1, -1):
        alpha = alphabet[size-k-1:size]
        letters = '-'.join(alpha[::-1] + alpha[1:])
        hyphens = (maxLength - len(letters))//2
        print('-'*hyphens + letters + '-'*hyphens)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

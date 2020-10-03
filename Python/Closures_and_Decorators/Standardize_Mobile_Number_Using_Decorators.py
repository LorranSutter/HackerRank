def wrapper(f):
    def fun(l):
        for k in range(len(l)):
            if(len(l[k]) == 10):
                l[k] = ' '.join(['+91', l[k][:5], l[k][5:]])
            if(len(l[k]) == 11):
                l[k] = ' '.join(['+91', l[k][1:6], l[k][6:]])
            if(len(l[k]) == 12):
                l[k] = ' '.join(['+91', l[k][2:7], l[k][7:]])
            if(len(l[k]) == 13):
                l[k] = ' '.join(['+91', l[k][3:8], l[k][8:]])
        f(l)
    return fun


# Another good solution
# def wrapper(f):
#     def phone(l):
#         f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
#     return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

if __name__ == '__main__':
    l = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    lowestGrade = min(l, key=lambda x: x[1])[1]
    l = [elem for elem in l if elem[1] != lowestGrade]
    secondLowestGrade = min(l, key=lambda x: x[1])[1]
    res = [elem for elem in l if elem[1] == secondLowestGrade]

    for elem in sorted(res, key=lambda x: x[0]):
        print(elem[0])

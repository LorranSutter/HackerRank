# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    K = int(input())

    rooms = {}
    for key in input().split():
        if key not in rooms.keys():
            rooms[key] = 1
        else:
            rooms[key] += 1

    for key in rooms.keys():
        if rooms[key] == 1:
            print(key)
            break

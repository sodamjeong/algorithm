for _ in range(int(input())):
    point = list(map(int,input().split()))
    point.sort()
    if point[3] - point[1] > 3:
        print('KIN')
    else:
        print(sum(point[1:4]))
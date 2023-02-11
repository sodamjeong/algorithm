for _ in range(int(input())):
    x,y = 1,0
    n = int(input())
    for _ in range(n):
        x,y = y,x+y
    print(x,y)

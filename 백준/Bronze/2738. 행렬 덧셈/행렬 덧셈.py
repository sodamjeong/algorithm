n,m = map(int,input().split())
lst = [input().split() for _ in range(n)]

for x in lst:
    plus = list(map(int,(input().split())))
    a = 0
    for y in x:
        print(int(y) + plus[a], end = ' ')
        a += 1
lst = [[0]*100 for i in range(100)]
cnt = 0

for i in range(4):
    n = list(map(int,input().split()))
    for x in range(n[0],n[2]):
        for y in range(n[1],n[3]):
            lst[x][y] = 1

for i in lst:
    cnt += i.count(1)
print(cnt)
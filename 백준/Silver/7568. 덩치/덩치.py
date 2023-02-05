people = [list(map(int,input().split())) for _ in range(int(input()))]
rank = []
for x in people:
    cnt = 1
    for y in people:
        if x[0]<y[0] and x[1]<y[1]:
            cnt += 1
    rank.append(cnt)
print(*rank)
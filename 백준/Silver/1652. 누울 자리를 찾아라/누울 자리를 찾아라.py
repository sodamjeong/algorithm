room = [list(input()) for _ in range(int(input()))]
n = len(room)
w = 0
h = 0
for i in room:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        else:
            if cnt > 1:
                w += 1
            cnt = 0
    if cnt > 1:
        w += 1
for x in range(n):
    cnt2 = 0
    for y in range(n):
        if room[y][x] == '.':
            cnt2 += 1
        else:
            if cnt2 > 1:
                h += 1
            cnt2 = 0
    if cnt2 > 1:
        h += 1
print(w, h)
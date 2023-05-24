n = int(input())
people = list(map(int,input().split()))
seat = [0]*n

for i,j in enumerate(people):
    cnt = 0
    for x,y in enumerate(seat):
        if y == 0 and cnt < j:
            cnt += 1
        elif y == 0 and cnt == j:
            seat[x] = i + 1
            break
print(*seat)
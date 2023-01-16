n = int(input())
m = list(map(int,input().split()))
a = 0

for x in m:
    cnt = 0
    if x == 1:
        pass
    else:
        for y in range(2,x + 1):
            if x % y == 0:
                cnt += 1
        if cnt == 1:
            a += 1

print(a)
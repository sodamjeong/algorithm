m = int(input())
n = int(input())
a = []

for i in range(m,n + 1):
    cnt = 0
    if i == 1:
        pass
    else:
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))
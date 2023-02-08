n = int(input())
cnt = 1
num = 0

while num <= n:
    num+=cnt
    if num >= n - cnt:
        break
    cnt += 1
print(cnt)
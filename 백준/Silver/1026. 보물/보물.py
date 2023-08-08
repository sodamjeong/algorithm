n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
cnt = 0

for i in range(n):
    cnt += (a[i] * b[-i-1])
print(cnt)
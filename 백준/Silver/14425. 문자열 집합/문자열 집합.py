import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [input().strip() for _ in range(n)]
lst2 = [input().strip() for _ in range(m)]
cnt = 0

for i in lst2:
    if i in lst:
        cnt += 1
print(cnt)
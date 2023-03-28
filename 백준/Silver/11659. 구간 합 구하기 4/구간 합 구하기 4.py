import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))

lst = [0]*(n+1)
cnt = 0

for i in range(1,n+1):
    cnt += num[i-1]
    lst[i] = cnt

for _ in range(m):
    x, y = map(int,input().split())
    print(lst[y] - lst[x-1])
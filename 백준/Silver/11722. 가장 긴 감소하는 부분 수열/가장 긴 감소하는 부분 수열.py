import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

ans = [1 for _ in range(n+1)]

for i in range(n):
  for j in range(i):
      if lst[i] < lst[j]:
        ans[i] = max(ans[i],ans[j]+1)
print(max(ans))
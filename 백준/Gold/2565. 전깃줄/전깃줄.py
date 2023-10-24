import sys
input = sys.stdin.readline

n = int(input())
ans = [1]*n
line = sorted([list(map(int,input().split())) for _ in range(n)])

for i in range(n):
    for j in range(i):
        if line[i][1]>line[j][1]:
            ans[i] = max(ans[i],ans[j]+1)

print(n - max(ans))
import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * n
lst = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
N = int(input())
memo = [0] * N
arr = [list(map(int, input().split())) for _ in range(N)]
if arr[N-1][0] == 1:
    memo[N-1] = arr[N-1][1]
for i in range(N-2, -1, -1):
    d = i + arr[i][0]
    if d == N:
        memo[i] = max(arr[i][1], memo[i+1])
    elif d < N:
        memo[i] = max([arr[i][1] + memo[d], memo[i+1]])
    elif d > N:
        memo[i] = memo[i+1]
print(memo[0])
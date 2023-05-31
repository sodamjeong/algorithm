dp = [[0]*i for i in range(1, 31)]

for i in range(30):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[M][N])  



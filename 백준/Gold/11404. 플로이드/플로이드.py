import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
INF = int(1e9)
bus = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    bus[a][b] = min(bus[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                bus[a][b] = 0
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if bus[a][b] == INF:
            bus[a][b] = 0
    print(*bus[a][1:])
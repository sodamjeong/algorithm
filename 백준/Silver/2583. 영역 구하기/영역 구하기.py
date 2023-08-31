import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m,n,k = map(int, input().split())

field = [[0] * n for _ in range(m)] 

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = 1

def dfs(x, y, cnt):
    field[y][x] = 1
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if (0 <= dx < n) and (0 <= dy < m) and field[dy][dx] == 0:
            cnt = dfs(dx, dy, cnt+1)
    return cnt

area = []
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(m):
    for x in range(n):
        if field[y][x] == 0:
            area.append(dfs(x, y, 1))

print(len(area))
print(*sorted(area))
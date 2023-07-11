import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = {-1: 0, 0: 0, 1: 0}


def divide(leng, x, y):
    start = graph[x][y]
    for i in range(x, x + leng):
        for j in range(y, y + leng):
            if start != graph[i][j]:
                for nx in range(x, x + leng, leng // 3):
                    for ny in range(y, y + leng, leng // 3):
                        divide(leng // 3, nx, ny)
                return
    cnt[start] += 1

divide(n, 0, 0)
print('\n'.join(map(str, cnt.values())))
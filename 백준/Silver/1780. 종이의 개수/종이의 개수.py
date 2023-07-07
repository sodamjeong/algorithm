import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = {-1: 0, 0: 0, 1: 0}


def divide(length, x, y):
    start = graph[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if start != graph[i][j]:
                for nx in range(x, x + length, length // 3):
                    for ny in range(y, y + length, length // 3):
                        divide(length // 3, nx, ny)
                return
    count[start] += 1

divide(N, 0, 0)
print('\n'.join(map(str, count.values())))
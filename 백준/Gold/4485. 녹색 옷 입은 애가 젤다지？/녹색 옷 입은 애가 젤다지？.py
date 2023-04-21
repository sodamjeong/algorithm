import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    direct = [(1,0),(-1,0),(0,1),(0,-1)]
    rupee = [[int(1e9)] * n for _ in range(n)]
    rupee[0][0] = field[0][0]
    queue = []

    heapq.heappush(queue,(0,0,rupee[0][0]))
    while queue:
        x,y,cost = heapq.heappop(queue)

        if rupee[x][y] < cost:
            continue
        for d in direct:
            xd, yd = x + d[0], y + d[1]
            if 0 <= xd < n and 0 <= yd < n:
                pay = field[xd][yd] + cost
                if pay < rupee[xd][yd]:
                    rupee[xd][yd] = pay
                    heapq.heappush(queue,(xd,yd,pay))
    return rupee


case = 0
while 1:
    case += 1
    n = int(input())
    if n == 0:
        break

    field = [list(map(int,input().split())) for _ in range(n)]
    print(f'Problem {case}: {dijkstra()[-1][-1]}')
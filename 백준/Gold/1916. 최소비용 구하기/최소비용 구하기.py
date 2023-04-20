import heapq
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int,input().split())
    bus[x].append((y,z))
start, end = map(int,input().split())

def dijkstra(bus, start):
    dist = [int(1e9)] * (n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        cd, cn = heapq.heappop(queue)
        if dist[cn] < cd:
            continue
        
        for tn,td in bus[cn]:
            cost = cd + td
            if dist[tn] > cost:
                dist[tn] = cost
                heapq.heappush(queue,(cost,tn))
    return dist[end]

print(dijkstra(bus,start))
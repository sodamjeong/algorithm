import sys
from collections import deque
input = sys.stdin.readline

N,M,R = map(int,input().split())
count = 1
graph = [[]*(N+1) for i in range(N+1)]
BFS = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global count
    q = deque([v])
    BFS[v] = 1

    while q:
        v = q.popleft()
        graph[v].sort(reverse = True)
        for i in graph[v]:
            if not BFS[i]:
                count += 1
                BFS[i] = count
                q.append(i)
bfs(R)

for i in BFS[1:]:
    print(i)
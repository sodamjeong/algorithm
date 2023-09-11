from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
link = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[r] = 1
cnt = 1
q = deque([r])

# 양방향 간선 생성
for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)

for i in range(1,n+1):
    link[i].sort()

while q:
    v = q.popleft()
    for i in link[v]:
        if visited[i]:
            continue
        cnt+=1
        visited[i] = cnt
        q.append(i)
print(*visited[1:], sep="\n")
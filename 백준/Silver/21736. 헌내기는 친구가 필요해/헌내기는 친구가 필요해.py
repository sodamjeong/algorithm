from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
start = ()

for i in range(N):
    row = list(input().rstrip())
    for j in range(M):
        if row[j] == 'I':
            start = (i, j)
    campus.append(row)
    
# BFS
direction = [(1,0), (0,1), (-1,0), (0,-1)]
visited = [[False]*M for _ in range(N)]
res = 0

queue = deque([start])
visited[start[0]][start[1]] = True
while(queue):
    x, y = queue.popleft()
    
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        
        if 0<=nx<N and 0<=ny<M:
            if campus[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                
                if campus[nx][ny] == 'P':
                    res += 1
                    
print(res if res > 0 else 'TT')
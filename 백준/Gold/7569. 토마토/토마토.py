import sys
from collections import deque
M,N,H = map(int,input().split())

a = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while de:
        z,x,y = de.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if(0 <= nx < N and 0 <= ny < M and 0 <= nz < H):
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = a[z][x][y] + 1
                    de.append([nz,nx,ny])

de = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if(a[i][j][k] == 1):
                de.append([i,j,k])

bfs()

cnt = 1
result = -1
for i in a:
    for j in i:
        for k in j:
            if k == 0:
                cnt = 0
            
            result = max(result,k)

if(cnt == 0):
    print(-1)
elif(result == 1):
    print(0)
else:
    print(result -1)
d = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(x,y,km,k):
    global cnt
    if km > cnt:
        cnt = km
    visited[x][y] = 1
    
    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 0:
            if mountain[nx][ny] < mountain[x][y]:
                dfs(nx,ny,km+1,k)
            elif k and k > mountain[nx][ny] - mountain[x][y]:
                high = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1
                dfs(nx,ny,km+1,0)
                mountain[nx][ny] = high
    visited[x][y] = 0

for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    mountain = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    top = max([max(i) for i in mountain])
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == top:
                dfs(i,j,1,k)
    print(f'#{t} {cnt}')
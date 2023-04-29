from collections import deque

n,m = map(int,input().split())
field = [list(map(int,input())) for _ in range(n)]
direct = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()

queue.append((0,0))
while queue:
  x,y = queue.popleft()
  for d in direct:
      xd, yd = x + d[0], y + d[1]
      if 0 <= xd < n and 0 <= yd < m:
          if field[xd][yd] == 1:
              field[xd][yd] = field[x][y] + 1
              queue.append((xd,yd))

print(field[-1][-1])
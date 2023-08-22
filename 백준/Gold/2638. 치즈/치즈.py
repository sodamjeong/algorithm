from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(n)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]

# 내부공기 확인
def check():
  visit = [[0]*m for _ in range(n)]
  que = deque()
  que.append((0,0))

  # 첫 시작점을 기준으로 연결되어있는 곳 모두 방문 처리
  while que:
    x,y = que.popleft()
    for d in dir:
      dx,dy = x+d[0], y+d[1]
      if 0 <= dx < n and 0 <= dy < m:
        if field[dx][dy] == 0 and visit[dx][dy] == 0 :
          que.append((dx,dy))
          visit[dx][dy] = 1

  # 필드가 0이고 방문처리가 안되어 있다면 내부공기
  for x in range(n):
    for y in range(m):
      if (field[x][y] + visit[x][y]) == 0:
        # 2로 갱신
        field[x][y] = 2

# 녹는 치즈 확인
def cheese():
  check()
  cheese  = []
  lst = []

  for x in range(n):
    for y in range(m):
      if field[x][y] == 1:
        cheese.append((x,y))
  
  for i in cheese:
    x,y,cnt = i[0], i[1], 0

    for d in dir:
      xd, yd = x+d[0], y+d[1]
      if 0 <= xd < n and 0 <= yd < m and field[xd][yd] == 0:
        cnt += 1
    if cnt > 1:
      lst.append((x,y))
  
  for j in lst:
      field[j[0]][j[1]] = 0
  
  for x in range(n):
    for y in range(m):
      if field[x][y] == 2:
        field[x][y] = 0

def day(d):
  some = 0
  for i in field:
    some += sum(i)
  if some == 0:
    print(d)
    return
  else:
    cheese()
    day(d+1)
    
day(0)
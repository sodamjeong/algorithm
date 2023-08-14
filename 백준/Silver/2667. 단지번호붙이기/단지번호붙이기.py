from collections import deque, Counter, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
field = [list(map(int,input().strip())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
direct = [(1,0),(0,1),(-1,0),(0,-1)]
queue = deque()
cnt = 0

for a in range(n):
  for b in range(n):
    if field[a][b] == 1 and visit[a][b] == 0:
        cnt += 1
        field[a][b] = cnt
        visit[a][b] = 1
        queue.append((a,b))
        while queue:
          x,y = queue.popleft()
          for d in direct:
            xd, yd = x + d[0], y + d[1]
            if 0 <= xd < n and 0 <= yd < n:
                if field[xd][yd] == 1 and visit[xd][yd] == 0:
                    field[xd][yd] = cnt
                    visit[xd][yd] = 1
                    queue.append((xd,yd))
print(cnt)
dic = defaultdict(int)
for i in field:
  for k,v in Counter(i).items():
    if k > 0 :
      dic[k] += v
sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1]))
for i in sorted_dict.values():
  print(i)
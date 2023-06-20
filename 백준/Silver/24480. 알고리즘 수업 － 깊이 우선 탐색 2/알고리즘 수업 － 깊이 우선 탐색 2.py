import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, num = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  global cnt
  cnt += 1
  visit[start] = cnt   
  for i in sorted(graph[start],reverse=True):
    if not visit[i]:
            dfs(i)

dfs(num)
print(*visit[1:],sep='\n')
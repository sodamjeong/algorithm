n = int(input())
m = int(input())
com = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    x,y = map(int,input().split())
    com[x] += [y]
    com[y] += [x]

def dfs(start):
    visited[start] = 1
    for j in com[start]:
        if visited[j] == 0:
            dfs(j)
dfs(1)
print(sum(visited)-1)
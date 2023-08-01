import sys
input = sys.stdin.readline

def dfs(x):
    if x == m:
        print(*res)
        return 

    for i in range(n): 
        if visited[i] == 0 : 
            res.append(lst[i]) 
            dfs(x+1)
            res.pop()
            visited[i] = 1 
            for j in range(i+1, n):
                visited[j] = 0
            
n, m = map(int, input().split())
lst=sorted(list(map(int,input().split())))
visited=[0]*n 
res = []
dfs(0)
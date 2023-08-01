import sys
input = sys.stdin.readline

def dfs(x):
    if x == m:
        print(*res)
        return 
    
    cnt = -1 

    for i in range(n): 
        if visited[i] == 0 and cnt != lst[i]: 
            visited[i] = 1 
            res.append(lst[i])
            cnt = lst[i]

            dfs(x+1)

            res.pop()
            visited[i] = 0
            
n, m = map(int, input().split())
lst=sorted(list(map(int,input().split())))
visited=[0]*n 
res = []
dfs(0)
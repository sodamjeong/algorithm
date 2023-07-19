import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M, R = map(int, input().split())
connection = [[] for _ in range(N+1)]        

for _ in range(M):                      
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)

for i in range(1, N+1):
    connection[i].sort()

order = [0] * (N+1)
visited = [0] * (N+1)
turn = 0
visited[R] = 1

def DFS(R):
    global turn                         

    turn += 1                           
    order[R] = turn  

    for i in connection[R]:
        if visited[i] == 0:
            visited[i] = 1
            DFS(i)

DFS(R)
order.pop(0) 
for ans in order:
    print(ans)



import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())

x = [[] for i in range(N+1)]
y = [0 for i in range(N+1)]

for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    x[a].append(b)
    x[b].append(a)

def DFS(start,x,y):
    for i in x[start]:
        if y[i] == 0:
            y[i] = start
            DFS(i,x,y)

DFS(1,x,y)
for i in range(2,N+1):
    print(y[i]) 

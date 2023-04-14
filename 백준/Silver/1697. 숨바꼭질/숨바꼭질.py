from collections import deque

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        m = queue.popleft()
        if m == k:
            print(visit[m])
            break
        for i in (m-1,m+1,m*2):
            if 0 <= i <= cnt and not visit[i]:
                visit[i] = visit[m] + 1
                queue.append(i)
                
cnt = 10 ** 5
visit = [0] * (cnt + 1)
n, k = map(int,input().split())
bfs()
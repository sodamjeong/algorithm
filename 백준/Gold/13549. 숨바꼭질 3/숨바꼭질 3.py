import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
visit = [0]*100001
visit[n] = 1
queue = [([0,n])]

while queue:
    time,site = heapq.heappop(queue)
    if site == m:
        print(time)
        break

    tel = site * 2
    if tel < len(visit) and not visit[tel]:
        visit[tel] = 1
        heapq.heappush(queue,(time,tel))
    
    for i in (site+1, site-1):
        if i >= 0 and i < len(visit) and not visit[i]:
            visit[i] = 1
            heapq.heappush(queue,(time+1,i))
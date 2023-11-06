import sys
import heapq
input = sys.stdin.readline

n = int(input())
visit = [0] * (n + 1)
computer = [[] for _ in range(n + 1)]
queue = [(0, 1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    computer[a].append((c, b))
    computer[b].append((c, a))

total,cnt = 0, 0
while queue and cnt < n:
    cost, com = heapq.heappop(queue)
    if not visit[com]:
        visit[com] = 1
        total += cost
        cnt += 1
        for i in computer[com]:
            heapq.heappush(queue, (i[0], i[1]))
print(total)
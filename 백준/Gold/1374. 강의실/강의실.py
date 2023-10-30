import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap, que = [], []

for _ in range(n):
    num, start, end = map(int,input().split())
    heapq.heappush(heap, [start,end])

heapq.heappush(que, heapq.heappop(heap)[1])

while heap:
    start, end = heapq.heappop(heap)
    if que[0] <= start:
        heapq.heappop(que)
    heapq.heappush(que, end)

print(len(que))
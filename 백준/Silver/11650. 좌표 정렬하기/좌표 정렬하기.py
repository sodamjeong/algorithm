import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x, y = map(int,input().split())
    heapq.heappush(heap,(x,y))
for _ in range(n):
    print(*heapq.heappop(heap))
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
prices = list(map(int, input().split()))

cost = 0
price = 1000000001
for i in range(n-1):
    price = min(price, prices[i])
    cost += (dist[i]* price)

print(cost)   
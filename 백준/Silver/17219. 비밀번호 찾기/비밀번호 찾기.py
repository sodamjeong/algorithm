import sys
input=sys.stdin.readline

n,m = map(int,input().split())
memo = {}
for _ in range(n):
    k,v = input().split()
    memo[k] = v
for _ in range(m):
    site = input().strip()
    print(memo[site])
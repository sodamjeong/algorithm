import sys
input = sys.stdin.readline
n, k = map(int,input().split())
up = down = 1
for i in range(k):
    up *= n - i
    down *= (i+1)
print(up//down)

import sys
input = sys.stdin.readline
n = int(input())
tile = [0, 1, 2]
for i in range(3,n+1):
    tile.append((tile[i-1]+tile[i-2])%10007)
print(tile[n])
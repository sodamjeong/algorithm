import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = sorted(list(map(int,input().split())))[::-1]
x,y = 1,tree[0]

while x <= y:
    mid = (x+y) // 2
    cnt = 0
    for i in tree:
        if i > mid:
            cnt += (i-mid)
    if cnt >= m:
        x = mid + 1
    elif cnt < m:
        y = mid - 1
print(y)
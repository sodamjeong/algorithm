import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [int(input()) for _ in range(n)]
x,y = 1,max(lst)

while x <= y:
    mid = (x+y) // 2
    line = 0
    for i in lst:
        line += (i//mid)
    if line < m:
        y = mid - 1
    else:
        x = mid + 1
print(y)
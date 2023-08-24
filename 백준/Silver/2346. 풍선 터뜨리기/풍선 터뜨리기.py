from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = deque(enumerate(map(int,input().split()),1))
ans = []
idx = 0
while arr:
    if idx > 0:
        a,b = arr.popleft()
        arr.append((a,b))
        idx -=1
    elif idx < 0:
        a,b = arr.pop()
        arr.appendleft((a,b))
        idx +=1
    else:
        a,b = arr.popleft()
        ans.append(a)
        if b > 0:
            idx = b-1
        else:
            idx = b
print(*ans)
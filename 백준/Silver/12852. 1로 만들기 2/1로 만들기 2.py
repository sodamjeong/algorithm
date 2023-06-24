import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
q=deque([[n]])
ans=[]
while q:
    x=q.popleft()
    y=x[0]
    if y==1:
        ans=x
        break
    if y%3==0:
        q.append([y//3]+x)
    if y%2==0:
        q.append([y//2]+x)
    q.append([y-1]+x)
print(len(ans)-1)
print(*ans[::-1])
from collections import deque
n=int(input())
q=deque(map(int,input().split()))
s=deque()
i=1
while q:
    if q and q[0]==i:
        q.popleft()
        i+=1
    else:
        s.append(q.popleft())
    while s and s[-1]==i:
        s.pop()
        i+=1
print('Sad' if s else 'Nice')
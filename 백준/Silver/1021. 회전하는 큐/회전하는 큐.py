from collections import deque
n,m = map(int,input().split())
lst = deque(range(1,n+1))
lst2 = deque(range(1,n+1))
num = list(map(int,input().split()))
answer = 0

for i in num:
    cnt = 0
    cnt2 = 0
    while 1:
        if lst[0] == i:
            lst.popleft()
            break
        lst.rotate(1)
        cnt += 1
    while 1:
        if lst2[0] == i:
            lst2.popleft()
            break
        lst2.rotate(-1)
        cnt2 += 1
    answer += min(cnt,cnt2)
print(answer)
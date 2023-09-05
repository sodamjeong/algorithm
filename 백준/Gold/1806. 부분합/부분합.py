import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

min = 100001
left,right = 0,1
cnt = lst[left]

while left < n:
    if cnt >= m:
        if (right - left) < min: 
            min = (right - left)
        cnt -= lst[left]
        left += 1

    if right == n and cnt < m:
        break

    if cnt < m:
        cnt += lst[right]
        right += 1

if min == 100001:
  print('0')
else:
  print(min)
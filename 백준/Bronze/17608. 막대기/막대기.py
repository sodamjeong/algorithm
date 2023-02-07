import sys
input = sys.stdin.readline

sticks = [int(input()) for _ in range(int(input()))]
stick = 0
cnt = 0
for i in sticks[::-1]:
    if i > stick:
        cnt += 1
        stick = i
print(cnt)
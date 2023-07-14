import sys
input = sys.stdin.readline

n = int(input())
a,b = 1, 2
cnt = 1 if n == 1 else 2

for i in range(3, n+1):
    cnt = (a + b) % 15746
    a, b = b, cnt
print(cnt)
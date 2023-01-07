X = int(input())
N = int(input())
d = 0

for i in range(N):
    a,b = map(int,input().split())
    d += (a * b)
if d == X:
    print('Yes')
else:
    print('No')
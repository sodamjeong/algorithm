import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

y = dict()

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a) >= m:
        if a in y:
            y[a] += 1
        else:
            y[a] = 1


y = sorted(y.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in y:
    print(i[0])
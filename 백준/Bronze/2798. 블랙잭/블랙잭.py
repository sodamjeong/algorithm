n,m = map(int,input().split())
card = list(map(int,input().split()))
c = []
for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1,n):
            t = card[x]+card[y]+card[z]
            if t <= m:
                c.append(t)
print(max(c))
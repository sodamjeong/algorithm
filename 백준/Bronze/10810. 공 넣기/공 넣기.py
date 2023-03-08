n,m = map(int,input().split())
basket = [0 for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    for j in range(x,y+1):
        basket[j] = z
print(*basket[1:])
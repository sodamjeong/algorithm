n,m = map(int,input().split())
basket = [i for i in range(n+1)]

for j in range(m):
    x,y = map(int,input().split())
    basket[x],basket[y] = basket[y], basket[x]
print(*basket[1:])
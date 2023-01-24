a,b = map(int,input().split())
n = []
for x in range(1,a+b):
    if a % x == 0 and b % x == 0:
        n.append(x)
m = max(n)        
print(m)
print(m*(a//m)*(b//m))
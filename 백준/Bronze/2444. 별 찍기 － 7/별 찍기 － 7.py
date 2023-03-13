n = int(input())
m = 0
for i in range(1,n+1):
    print((' '*(n-i))+(i+m)*'*')
    m += 1
m-=1
for j in range(n-1,0,-1):
    m -= 1
    print((' '*(n-j))+(j+m)*'*')
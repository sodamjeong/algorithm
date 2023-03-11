n,m = map(int,input().split())
b = list(range(n+1))

for _ in range(m):
    i,j = map(int,input().split())
    num = 0
    while 1:
        b[i+num],b[j-num]=b[j-num],b[i+num]
        num += 1
        if i+num >= j-num:
            break
print(*b[1:])
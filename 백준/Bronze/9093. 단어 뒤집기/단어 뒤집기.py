m=[]

for i in range(int(input())):
    n = list(input().split())
    for x in n:
        m.append(x[::-1])
    print(*m)
    m=[]
n = [1, 2, 3, 4, 5]
m = list(map(int,input().split()))

while n != m:
    a = 1
    for i in m:
        try:
            if i > m[a]:
                m.remove(i)
                m.insert(a,i)
                a += 1
                print(*m)
            elif i < m[a]:
                a += 1
        except:
            pass
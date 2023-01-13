def d(n):
    return i + sum(map(int,str(i)))

a = []

for i in range(1, 10001):
        a.append(d(i))

a.sort()

for n in range(1,10001):
    if n not in a:
        print(n)
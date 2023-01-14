t = int(input())
x = []
y = []

for i in range(t):
    a,b = input().split()
    for n in b:
        x.append(n)
    for m in x:
        y.append(m*int(a))
    print(''.join((y)))
    x.clear()
    y.clear()
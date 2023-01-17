x = {}
y = {}

for i in range(3):
    a, b = list(map(int,input().split()))
    if a not in x:
        x[a] = 1
    else:
        x[a] +=1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1

for v in x:
    if x[v] == 1:
        print(v,end=' ')
        for v2 in y:
            if y[v2] == 1:
                print(v2)

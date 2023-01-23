n = sorted(set([input() for _ in range(int(input()))]))
m = []
for x in range(51):
    for y in n:
        if len(y) == x:
            m.append(y)
print(*(m),sep='\n')
n = sorted(set([input() for _ in range(int(input()))]))
for x in range(51):
    for y in n:
        if len(y) == x:
            print(y)
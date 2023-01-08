t = int(input())

for i in range(t):
    n = 0
    m = 0
    ox = list(input())
    for num in ox:
        if num == 'O':
            n += 1
            m += n
        else:
            n = 0
    print(m)
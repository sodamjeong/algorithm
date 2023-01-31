n = [list(input()) for _ in range(5)]

for x in range(16):
    for y in range(5):
        try:
            print(n[y][x],end='')
        except:
            pass
n = [i for i in input()]

while len(n) > 0:
    print(''.join(n[0:10]))
    del(n[0:10])
a, b = map(int,(input().split()))

if (a - b) < 0:
    if b == 3 and a == 1:
        print('A')
    else:
        print('B')
else:
    if a == 3 and b == 1:
        print('B')
    else:
        print('A')
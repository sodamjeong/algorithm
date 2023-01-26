n = [int(input()) for i in range(3)]
if sum(n) != 180:
    print('Error')
else:
    if len(set(n)) == 1:
        print('Equilateral')
    elif len(set(n)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
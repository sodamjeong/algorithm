n = []
for i in range(int(input())):
    a,b = input(). split()
    for x in b:
        n.append(x*int(a))
    print(''.join(n))
    n = []
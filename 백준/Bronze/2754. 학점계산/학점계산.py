n = list(input())
i = float('FDCBA'.index(n[0]))

if len(n)==1:
    print(i)
else:
    if n[1] == '+':
        print(i+0.3)
    elif n[1] == '-':
        print(i-0.3)
    else:
        print(i)
for i in range(int(input())):
    n = input()
    m = []
    try:
        for x in n:
            if x == '(':
                m.append(x)
            else:
                m.pop()
        if len(m) == 0:
            print('YES')
        else:
            print('NO')
    except IndexError:
        print('NO')
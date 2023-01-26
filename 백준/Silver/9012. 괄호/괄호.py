for i in range(int(input())):
    n = input()
    cnt = 0
    for x in n:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')
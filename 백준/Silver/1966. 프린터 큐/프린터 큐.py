for _ in range(int(input())):
    n,m = map(int,input().split())
    num = list(map(int,input().split()))
    lst = [(i, idx) for idx, i in enumerate(num)]
    cnt = 0

    while 1:
        if max(lst)[0] == lst[0][0]:
            cnt += 1
            if lst[0][1] == m:
                print(cnt)
                break
            else:
                lst.pop(0)
        else:
            lst.append(lst.pop(0))

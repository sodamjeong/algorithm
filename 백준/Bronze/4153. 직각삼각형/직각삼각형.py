while 1:
    n = list(map(int,input().split()))
    m = sorted(n)
    if sum(m) == 0:
        break
    if m[2]**2 == (m[0]**2+m[1]**2):
        print('right')
    else:
        print('wrong')
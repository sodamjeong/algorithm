for _ in range(int(input())):
    x,y = map(int,input().split())
    n = [list(input().split()) for _ in range(x)]
    new_n = [[0]*x for _ in range(y)]
    cnt = 0
    for i in range(y):
        for j in range(x):
            new_n[i][j]=n[j][y-i-1]
    for a in new_n:
        for b in range(len(a)):
            if a[b] == '1':
                cnt += a[b:].count('0')
            else:
                pass
    print(cnt)
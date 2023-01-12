t = int(input())
day = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }

for i in range(1, t + 1):
    n = input()
    a = n[:4]
    b = n[4:6]
    c = n[6:]
    if int(b) not in day:
        print(f'#{i}',-1)
    else:
        if int(c) > day[int(b)] or int(c) <= 0:
            print(f'#{i}',-1)
        else:
            print(f'#{i}',a+'/'+b+'/'+c)
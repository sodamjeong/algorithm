for i in range(int(input())):
    n = list(map(int,input().split()))
    a = sorted(n)
    if a[0] == a[1]:
        print(f'#{i+1} {a[2]}')
    else:
        print(f'#{i+1} {a[0]}')
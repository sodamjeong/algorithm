def power(n,m):
    global num
    if m < 2:
        return num
    else:
        num *= n
        return(power(n,m-1))

for _ in range(10):
    t = int(input())
    n,m = map(int,input().split())
    num = n
    print(f'#{t}',power(n,m))
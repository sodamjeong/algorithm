for t in range(1,int(input())+1):
    a,b = map(int,input().split())
    if a+b < 24:
        print(f'#{t} {a+b}') 
    else:
        print(f'#{t} {(a+b)-24}')
for t in range(1,int(input())+1):
    x,y,z = map(int,input().split())
    if x > z:
        print(f'#{t} {x-z}')
    elif z > y:
        print(f'#{t} -1')
    else:
        print(f'#{t} 0')
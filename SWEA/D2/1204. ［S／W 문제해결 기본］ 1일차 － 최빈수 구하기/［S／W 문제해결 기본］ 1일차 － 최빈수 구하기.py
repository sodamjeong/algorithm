for i in range(int(input())):
    t = int(input())
    m = list(map(int,input().split()))
    n ={}
     
    for a in m:
        if a not in n:
            n[a] = 1
        else :
            n[a] += 1
 
    print(f'#{t}', max([k for k in n if n[k] == max([v for v in n.values()])]))

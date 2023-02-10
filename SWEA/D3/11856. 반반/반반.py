for t in range(1,int(input())+1):
    n = input()
    m = {}
    for i in n:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    if len(m) == 2 and len(set(m.values()))==1:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')

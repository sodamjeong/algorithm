for t in range(1,11):
    n = int(input())
    m = list(map(int,input().split()))
    for i in range(n):
        m.append(m.pop(m.index(max(m)))-1)
        m.append(m.pop(m.index(min(m)))+1)
    print(f'#{t}',max(m)-min(m))
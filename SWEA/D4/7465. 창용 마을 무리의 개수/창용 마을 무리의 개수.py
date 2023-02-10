for t in range(1,int(input())+1):
    n,m = map(int,input().split())
    p = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        p[a] += [b]
        p[b] += [a]
    visited = [0] * (n+1)
    stack = []
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            cnt += 1
            stack.append(i)
            visited[i] == 1
        while stack:
            num = stack.pop()
            for j in p[num]:
                if visited[j] == 0:
                    stack.append(j)
                    visited[j] = 1
    print(f'#{t} {cnt}')
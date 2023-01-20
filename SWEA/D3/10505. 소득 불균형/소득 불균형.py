for i in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int,input().split()))
    m = [x for x in lst if x <= (sum(lst)/n)]
    print(f'#{i} {len(m)}')
C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    M = sum(N[1:])/N[0]
    cnt = 0
    for score in N[1:]:
        if score > M:
            cnt += 1
    B = cnt/N[0] * 100 
    print(f'{B:.3f}%')


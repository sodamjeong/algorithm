C = int(input())

for i in range(C):
    score = list(map(int,input().split()))
    n = sum(score[1:])/score[0]
    m = 0
    for a in score[1:]:
        if a > n :
            m += 1
    percent = m / score[0] * 100
    print(f'{percent:.3f}%')
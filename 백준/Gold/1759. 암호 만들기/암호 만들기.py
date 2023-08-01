from itertools import combinations
n,m = map(int,input().split())
lst = sorted(input().split())

for i in combinations(lst,n):
    cnt = 0
    for j in i:
        if j in 'aeiou':
            cnt += 1

    if cnt >= 1 and cnt <= n - 2:
        print(''.join(i))
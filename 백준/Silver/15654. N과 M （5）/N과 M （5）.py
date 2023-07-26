from itertools import permutations
n,m= map(int,input().split())
num = sorted(list(map(int,input().split())))

for i in permutations(num,m):
    print(*i)
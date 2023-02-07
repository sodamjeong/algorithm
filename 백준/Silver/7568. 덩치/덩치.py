import sys
input = sys.stdin.readline
physical = [list(map(int,input().split())) for _ in range(int(input()))]

for i in physical:
    rank = 1 
    for j in physical:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank,end=' ')
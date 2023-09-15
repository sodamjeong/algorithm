import sys
input = sys.stdin.readline
n = int(input())

lst = [ list(map(int, input().split())) for _ in range(n) ]
lst2 = [ [0]*i for i in range(1,n+1) ]
lst2[0][0] = lst[0][0]

for i in range(1,n):
    for j in range(i):
        lst2[i][j] = max(lst2[i][j], lst2[i-1][j] + lst[i][j])
        lst2[i][j+1] = max(lst2[i][j+1], lst2[i-1][j] + lst[i][j+1])

print(max(lst2[n-1]))
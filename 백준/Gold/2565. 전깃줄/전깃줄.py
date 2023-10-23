import sys
input = sys.stdin.readline

n=int(input())
ans=[1]*n
lst=sorted([list(map(int,input().split())) for _ in range(n)])

for i in range(1,n):
    for j in range(0,i):
        if lst[i][0]>lst[j][0] and lst[i][1]>lst[j][1]:
            ans[i]=max(ans[i],ans[j]+1)

print(n-max(ans))
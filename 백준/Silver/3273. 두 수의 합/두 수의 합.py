import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()
x = int(input())
i,j,cnt=0,n-1,0
while(True):
    if a[i]+a[j] == x:
        cnt+=1 
    if a[i] + a[j] < x:
        i+=1
    else:
        j-=1
    if i >= j:
        break
print(cnt)
n,m = map(int,input().split())
lst = list(range(1,n+1))
num = list(map(int,input().split()))
cnt = 0

for i in num:
    x = lst.index(i)
    cnt += min(x,len(lst)-x)
    lst = lst[x+1:] + lst[:x]
print(cnt)
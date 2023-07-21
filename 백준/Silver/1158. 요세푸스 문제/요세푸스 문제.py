n,m = map(int,input().split())
lst = [ i for i in range(1,n+1)]
num = []
cnt = 0
for i in range(n):
    cnt += m - 1
    if cnt >= len(lst):
        cnt %= len(lst)
    num.append(str(lst.pop(cnt)))
print("<",", ".join(num),">",sep='')
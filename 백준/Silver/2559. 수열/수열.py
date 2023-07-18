n, m = map(int,input().split())
temp = list(map(int, input().split()))
lst=[]
lst.append(sum(temp[:m]))

for i in range(n-m):
    lst.append(lst[i]-temp[i]+temp[i+m])

print(max(lst))

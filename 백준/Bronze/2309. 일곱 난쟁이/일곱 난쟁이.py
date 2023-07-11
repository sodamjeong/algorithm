lst=[int(input()) for _ in range(9)]
n,m = 0,0

total = sum(lst)
for i in range(8):
  for j in range(i+1, 9):
    if total-(lst[i]+lst[j])==100:
      n,m=lst[i],lst[j]
lst.remove(n)
lst.remove(m)
lst.sort()

for i in lst:
  print(i)
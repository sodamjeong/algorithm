data=[]
one=0
two=0

for _ in range(9):
  data.append(int(input()))
  
sum_val=sum(data)
for i in range(8):
  for j in range(i+1, 9):
    if sum_val-(data[i]+data[j])==100:
      one=data[i]
      two=data[j]
data.remove(one)
data.remove(two)
data.sort()

for i in data:
  print(i)
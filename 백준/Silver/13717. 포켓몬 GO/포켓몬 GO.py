cnt = 0
mon = ['',0]

for _ in range(int(input())):
  n,m = input(), 0
  a,b = map(int,input().split())

  while b / a >= 1:
    m += (b//a)
    b = (b%a) + ((b//a)*2)
  cnt+= m
  if m > mon[1]:
    mon[0],mon[1] = n,m

print(cnt,mon[0],sep='\n')
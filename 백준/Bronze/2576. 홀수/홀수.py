s = []
for i in range(7):
    if (n:=int(input())) % 2 == 1:
        s.append(n)
if len(s)==0:
    print('-1')
else:
    print(f'{sum(s)}\n{min(s)}')
a,b = map(int,input().split())
name = {}
m = []
cnt = 0

for i in range(a+b):
    n = input()
    if n not in name:
        name[n] = 1
    else:
        name[n] += 1
for k,v in name.items():
    if v==2:
        cnt += 1
        m.append(k)
print(cnt)
print(*sorted(m),sep="\n")
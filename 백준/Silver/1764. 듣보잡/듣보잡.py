import sys
input = sys.stdin.readline

a,b = map(int,input().split())
name = {}
lst = []

for i in range(a+b):
    n = input().strip()
    if n not in name:
        name[n] = 1
    else:
        name[n] += 1
for k,v in name.items():
    if v==2:
        lst.append(k)
print(len(lst),*sorted(lst),sep='\n')
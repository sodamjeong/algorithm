n = int(input())
x = list(map(int,input().split()))
n = 0
m = []

for i in x:
    if i == 1:
        n += 1
        m.append(n)
    else:
        n = 0

print(sum(m))
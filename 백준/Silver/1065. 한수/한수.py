def han(x):
    a = str(x)
    if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
        return x

N = int(input())
n = []

for i in range(1,N+1):
    if i >= 100:
        n.append(han(i))
    else:
        n.append(i)

print(len(n)-n.count(None))
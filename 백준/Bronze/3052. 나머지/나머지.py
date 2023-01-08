n = []
m = {}
e = 0

for i in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

for num in n:
    if num not in m:
        m[num] = 1
    else:
        m[num] += 1

for k in m:
    e += 1

print(e)
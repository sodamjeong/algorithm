n = int(input())
m = []

for i in range(1, 1001):
    if n % i == 0:
        m.append(i)
print(*m)
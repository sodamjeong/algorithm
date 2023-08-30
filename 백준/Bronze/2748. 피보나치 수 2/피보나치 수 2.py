n = int(input())
m = [0] * (n+1)
m[1] = 1
for i in range(2, n+1):
    m[i] = m[i-1] + m[i-2]
print(m[n])
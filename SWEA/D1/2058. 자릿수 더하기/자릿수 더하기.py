n = int(input())
m = 0
while n > 0:
    m += n % 10
    n //= 10
print(m) 
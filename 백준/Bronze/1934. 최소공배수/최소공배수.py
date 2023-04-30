import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = lcm(a, b)
    print(result)
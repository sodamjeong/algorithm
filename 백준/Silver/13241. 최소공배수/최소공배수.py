def uclid_lcm(a, b):
    x, y = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = x % y
        x, y = y, r
    return a * b // x

A, B = map(int, input().split())
print(uclid_lcm(A, B))
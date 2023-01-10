a, b = map(int,input().split())
n = (a + b, a - b, a * b, int(a / b))

for i in n:
    print(i)
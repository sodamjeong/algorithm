X = int(input())
Y = X
n = 0

while True:
    a = Y // 10
    b = Y % 10
    c = (a + b) % 10
    Y = b * 10 + c
    n += 1
    if Y == X:
        print(n)
        break
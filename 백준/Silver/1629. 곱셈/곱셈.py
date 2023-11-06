a, b, c = map(int, input().split())


def divide(b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return divide(b//2) ** 2 % c
    if b % 2 == 1:
        return a * (divide(b//2) ** 2) % c


print(divide(b))
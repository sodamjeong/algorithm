money = [25, 10, 5, 1]

for i in range(int(input())):
    n = int(input())
    num = []
    for x in money:
        num.append(n//x)
        n -= (x*(n//x))
    print(*num)
a = int(input())
b = int(input())
c = int(input())
n = str(a*b*c)

for x in range(10):
    for y in n:
        print(n.count(str(x)))
        break
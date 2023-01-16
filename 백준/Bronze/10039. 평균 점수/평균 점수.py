x =[]
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    x.append(n)

print(sum(x)//5)
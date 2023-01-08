n = []
a = list(range(1,31))

for i in range(28):
    b = int(input())
    n.append(b)

for num in a:
    if num not in n:
        print(num)
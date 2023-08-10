from collections import Counter
num = Counter([int(input()) for _ in range(5)])

for x,y in num.items():
    if y % 2 == 1:
        print(x)

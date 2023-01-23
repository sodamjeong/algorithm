n = int(input())
for i in range(n+2):
    m = list(str(i))
    num = i + sum(map(int,m))
    if i > n:
        print(0)
    else:
        if n == num:
            print(i)
            break
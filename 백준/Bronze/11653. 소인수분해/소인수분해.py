n = int(input())

for x in range(2, n + 1):
    if n == 1:
        print(-1)
    else:
        while n % x == 0:
            print(x)
            n /= x
            if n / x == 1 and n % x == 0:
                print(x)
                break
        if n == 1:
            break
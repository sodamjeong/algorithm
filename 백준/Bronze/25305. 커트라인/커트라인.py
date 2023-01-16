n, k = map(int,input().split())
x = list(map(int,(input().split())))

if k == 1:
    print(*sorted(x)[-k:])
else:
    print(*sorted(x)[-k:-k+1])
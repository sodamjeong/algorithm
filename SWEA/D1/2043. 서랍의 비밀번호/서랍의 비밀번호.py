p, k = map(int,input().split())

if k > p :
    print(999 - k + p + 2)
else:
    print(p - k + 1)
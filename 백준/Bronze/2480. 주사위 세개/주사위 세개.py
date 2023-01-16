a, b, c = map(int,input().split())
x = [a, b, c]
y = sorted(x)

if len(set(x)) == 1:
    print(10000 + (1000 * y[1]))
elif len(set(x)) == 2 :
    print(1000 + (100 * y[1]))
else:
    print(100 * y[2])
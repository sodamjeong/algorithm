t = int(input())
num = {'0','1','2','3','4','5','6','7','8','9'}
m = 1
b = []

for i in range(1,t+1):
    n = int(input())
    while num != set(b):
        a = n * m
        m += 1
        for x in str(a):
            if x not in b:
                b.append(x)
    print(f'#{i}',a)
    b = []
    m = 1
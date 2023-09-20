L1 = [1] * 101
L1[4] = 2
L1[5] = 2

for i in range(6,101):
    L1[i] = L1[i-5] + L1[i-1]

T = int(input())
for i in range(T):
    N = int(input())
    print(L1[N])
import sys
import math

def eratos(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [x for x in range(n + 1) if is_prime[x]]

x = set(eratos(1000000))

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a = int(sys.stdin.readline())
    if a == 4:
        print(1)
        continue
    cnt = 0
    for i in range(3, a // 2 + 1, +2):
        if i in x and a - i in x:
            cnt += 1
    print(cnt)
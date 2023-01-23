import sys
input = sys.stdin.readline

def prime(n):
    m = []
    lst = list(range((n*2)+1))
    for i in lst[2:]:
        if lst[i] > n:
            m.append(i)
        lst[i::i] = ((n*2)//i) * [0]
    print(len(m))

while 1:
    n = int(input())
    if n == 0:
        break
    else:
        prime(n)
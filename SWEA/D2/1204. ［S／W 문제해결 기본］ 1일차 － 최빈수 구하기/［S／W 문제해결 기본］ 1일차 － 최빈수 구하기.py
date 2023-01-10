t = int(input())
n ={}
value = []
key = []

for i in range(1,t+1):
    tt = int(input())
    m = list(map(int,input().split()))
    for a in m:
        if a not in n:
            n[a] = 1
        else :
            n[a] += 1
    for v in n.values():
        value.append(v)
    for k in n:
        if n[k] == max(value):
            key.append(k)
    print(f'#{tt}', max(key))
    n = {}
    value = []
    key = []
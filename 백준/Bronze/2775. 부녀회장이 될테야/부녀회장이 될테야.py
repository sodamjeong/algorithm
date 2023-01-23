for _ in range(int(input())):
    n = [i for i in range(1,15)]
    h = int(input())
    r = int(input())
    for x in range(h):
        m = []
        for y in range(1,r+1):
            m.append(sum(n[0:y]))
        n = m
    print(n[-1])

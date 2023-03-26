for t in range(int(input())):
    item = {}
    cnt = 1
    for i in range(int(input())):
        n, m = input(). split()
        if m not in item:
            item[m] = 2
        else:
            item[m] += 1
    for v in item.values():
        cnt *= v
    print(cnt-1)
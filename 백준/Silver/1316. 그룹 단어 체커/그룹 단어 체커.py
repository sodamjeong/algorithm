cnt = 0
for _ in range(int(input())):
    n = input()
    m = []
    for i in range(len(n)):
        if n[i] not in m:
            m.append(n[i])
        else:
            if n[i] == n[i-1]:
                m.append(n[i])
            else:
                m.clear()
                break
    if len(m) > 0:
        cnt += 1
print(cnt)
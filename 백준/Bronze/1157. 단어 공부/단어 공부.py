n = input().upper()
m = {}
value = []
key =[]
for i in n:
    if i not in m:
        m[i] = 1
    else:
        m[i] += 1

for a in m:
    value.append(m[a])

for b in m:
    if m[b] == max(value):
        key.append(b)

if len(key) > 1:
    print('?')
else:
    print(*key)
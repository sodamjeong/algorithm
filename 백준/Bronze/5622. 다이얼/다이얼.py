n = input()
m = {
    'ABC':3,'DEF':4,'GHI':5,
    'JKL':6,'MNO':7,'PQRS':8,
    'TUV':9,'WXYZ':10
}
time = []
for x in n:
    for y in m:
        if x in y:
            time.append(m.get(y))
print(sum(time))
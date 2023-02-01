part = 666
series = int(input())
cnt = 0
while 1:
    if ('666') in str(part):
        cnt += 1
        if cnt == series:
            break
    part += 1
print(part)
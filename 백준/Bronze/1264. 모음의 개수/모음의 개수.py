n = ['a','e','i','o','u']
while 1:
    cnt = 0
    for i in (m:=input().lower()):
        if i in n:
            cnt += 1
    if m == '#':
        break
    print(cnt)
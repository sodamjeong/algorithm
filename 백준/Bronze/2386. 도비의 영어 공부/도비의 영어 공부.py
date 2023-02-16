while 1:
    n = input().lower()
    if n == '#':
        break
    print (n[0], n[1:].count(n[0]))
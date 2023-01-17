n = int(input())
m = n
cnt = 0

while 1:
    a = m // 10
    b = m % 10
    m = (b * 10) + ((a + b) % 10)
    cnt += 1
    if m == n:
        print(cnt)
        break
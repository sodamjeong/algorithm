import sys

while True:
    a,b = map(int,sys.stdin.readline().split())
    c = a + b
    if c == 0:
        break
    else:
        print(c)
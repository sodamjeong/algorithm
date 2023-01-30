import sys
input = sys.stdin.readline

a,b = input().split()
c = 0

for x in a:
    for y in b:
        c += int(x)*int(y)
print(c)
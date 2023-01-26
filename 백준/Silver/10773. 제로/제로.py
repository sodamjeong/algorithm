import sys
input = sys.stdin.readline

n = []
for i in range(int(input())):
    m = int(input())
    if m > 0 :
        n.append(m)
    else:
        n.pop()
print(sum(n))
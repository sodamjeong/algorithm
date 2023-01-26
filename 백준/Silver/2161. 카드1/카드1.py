import sys
input = sys.stdin.readline

n = [i for i in range(1,int(input())+1)]
m = []
while len(n) > 1:
    m.append(n.pop(0))
    n.append(n.pop(0))
print(*m,*n)
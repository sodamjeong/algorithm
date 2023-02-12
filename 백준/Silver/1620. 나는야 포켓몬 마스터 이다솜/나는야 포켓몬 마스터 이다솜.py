import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mon = {}
mon2 = {}

for i in range(1,n+1):
    p = input().rstrip('\n')
    mon[str(i)] = p
    mon2[p] = i
for i in range(m):
    s = input().rstrip('\n')
    print(mon.get(s,mon2.get(s)))

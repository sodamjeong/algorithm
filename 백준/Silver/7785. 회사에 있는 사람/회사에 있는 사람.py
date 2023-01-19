import sys
input = sys.stdin.readline
office = {}

for i in range(int(input())):
    log = input().split()
    if log[0] not in office:
        office[log[0]] = 1
    else:
        del office[log[0]]

print(*sorted(office)[::-1],sep='\n')
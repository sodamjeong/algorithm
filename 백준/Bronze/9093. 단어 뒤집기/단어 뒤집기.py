import sys
input = sys.stdin.readline
for i in range(int(input())):
    print(*[s[::-1] for s in input().split()])
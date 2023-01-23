import sys
input=sys.stdin.readline

print(*sorted([int(input()) for i in range(int(input()))]),sep='\n')
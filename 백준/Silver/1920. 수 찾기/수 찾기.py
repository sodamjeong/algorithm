import sys
input = sys.stdin.readline

input()
lst = {i : 1 for i in list(map(int,input().split()))}
input()
for i in list(map(int,input().split())):
    print(lst.get(i,0))
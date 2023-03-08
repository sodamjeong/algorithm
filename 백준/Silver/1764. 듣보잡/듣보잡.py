import sys
input = sys.stdin.readline

a,b = map(int,input().split())
p1 = [input().strip() for _ in range(a)]
p2 = [input().strip() for _ in range(b)]
lst = set(p1)&set(p2)
print(len(lst),*sorted(lst),sep='\n')
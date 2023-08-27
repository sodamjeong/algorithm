import sys
n=int(input())
s=[]
for i in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    if l[0]==1:
        s.append(l[1])
    elif l[0]==2:
        print(s.pop() if len(s) else -1)
    elif l[0]==3:
        print(len(s))
    elif l[0]==4:
        print(0 if len(s) else 1)
    else:
        print(s[-1] if len(s) else -1)
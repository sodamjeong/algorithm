N, X = map(int,input().split())
A = list(map(int,input().split()))
n = []

for i in A:
    if i < X:
        n.append(i)

for a in n:
    print(a,end=" ")
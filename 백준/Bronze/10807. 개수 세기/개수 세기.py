N = int(input())
n = list(map(int,input().split()))
v = int(input())
x = 0

for i in n:
    if i == v:
        x += 1

print(x)
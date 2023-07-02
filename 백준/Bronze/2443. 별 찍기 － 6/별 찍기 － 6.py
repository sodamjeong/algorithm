n=int(input())
x=1
for i in range(n):
    print(" "*i+"*"*(2*n-x))
    x+=2
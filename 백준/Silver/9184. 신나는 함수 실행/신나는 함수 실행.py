import sys

D1 = dict()

def w(a,b,c):
    if D1.get((a,b,c)) != None:
        return D1[(a,b,c)]
    elif (a<=0) or (b<=0) or (c<=0):
        return 1
    elif (20<a) or (20<b) or (20<c):
        return w(20,20,20)
    elif (a<b) and (b<c):
        Ans = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        D1[(a,b,c)] = Ans
        return Ans
    else:
        Ans = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        D1[(a,b,c)] = Ans
        return Ans

while True:
    A,B,C = map(int, sys.stdin.readline().split())

    if (A==-1) and (B==-1) and (C==-1):
        break
    else:
        print("w({0}, {1}, {2}) = {3}".format(A,B,C,w(A,B,C)))
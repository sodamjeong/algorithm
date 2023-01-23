import sys
input = sys.stdin.readline

def prime(i):
    if i < 10:
        if i in [2,3,5,7]:
            return True
    else:
        for x in range(2,int(i**0.5)+1):
            if i % x == 0:
                return False
        return True

m,n = map(int,input().split())

for i in range(m,n+1):
    if prime(i):
        print(i)
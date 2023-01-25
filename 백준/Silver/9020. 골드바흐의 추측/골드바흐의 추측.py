import sys 
input = sys.stdin.readline

def prime(n):
    if n == 2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

for x in range(int(input())):
    n = int(input())
    a = b = int(n/2)
    while True:
        if prime(a) and prime(b):
            print(a,b);break
        elif a == 0: break
        else:
            a -= 1
            b += 1
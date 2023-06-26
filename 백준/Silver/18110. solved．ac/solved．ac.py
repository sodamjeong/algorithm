import sys
input = sys.stdin.readline

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
n = int(input())  

if n:
    opinion = sorted([int(input()) for _ in range(n)])
    start = round(n * 0.15)  
    score = opinion[start:n - start]  
    print(round(sum(score) / len(score)))  
else:
    print(0)
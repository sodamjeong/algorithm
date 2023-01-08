n = int(input())
a = list(map(int,input().split()))

print(round(((sum(a)/n)/max(a))*100,3))
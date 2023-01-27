n = sorted(set([input() for _ in range(int(input()))]))
print(*sorted(n,key=len),sep='\n')
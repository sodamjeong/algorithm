n = int(input())
print(*[' '*i+'*'*(n-i) for i in range(n)],sep='\n')
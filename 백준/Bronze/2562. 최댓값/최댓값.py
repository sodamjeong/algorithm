A = []

for i in range(9):
    a = int(input())
    A.append(a)

print(max(A)) 
print(A.index(max(A))+1)
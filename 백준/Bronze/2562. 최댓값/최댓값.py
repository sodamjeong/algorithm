A = []
B = 1

for i in range(9):
    a = int(input())
    A.append(a)

for n in A:
    if n != max(A):
        B += 1
    else:
        print(max(A))
        print(B)
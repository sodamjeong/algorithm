A, B = map(int,input().split())
C = int(input())
D = B + C
H = int(((A * 60) + D) / 60)
M = ((A * 60) + D) % 60

if H >= 24:
    H -= 24

print(H, M)
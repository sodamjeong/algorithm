import sys
input = sys.stdin.readline
a = int(input())
alpa = input()
n = [0] * a
m = 1234567891

for i in range(a):
    num = ord(alpa[i]) - ord('a') + 1
    n[i] = num

for j in range(a):
    ri = 31**j
    n[j] *= ri
print(sum(n) % m)
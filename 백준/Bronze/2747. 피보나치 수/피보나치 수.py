import sys
input = sys.stdin.readline

n = int(input())
lst = [0, 1]

if n == 1 or n == 2:
  print(1)
else:
  for i in range(n-1):
    lst.append(lst[i]+lst[i+1])
  print(lst[-1])
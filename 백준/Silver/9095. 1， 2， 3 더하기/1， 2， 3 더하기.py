import sys
from collections import deque
input = sys.stdin.readline

def sol(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4
    return sol(num-1) + sol(num-2) + sol(num-3)
T = int(input())

for i in range(T):
    num = int(input())
    print(sol(num))
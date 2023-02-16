from collections import Counter
import sys
input = sys.stdin.readline

input()
n = list(map(int,input().split()))
input()
card = Counter(n)
for i in list(map(int,input().split())):
    print(card.get(i,0),end=' ')
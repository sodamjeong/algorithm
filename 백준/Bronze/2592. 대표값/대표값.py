from collections import Counter
import sys
input=sys.stdin.readline
n = [int(input()) for _ in range(10)]
print(sum(n)//10)
print(Counter(n).most_common()[0][0])
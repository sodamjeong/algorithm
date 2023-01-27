from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()
dic = Counter(m).most_common(2)

print(round(sum(m)/n))
print(m[n//2])
if len(m) > 1:
    if dic[0][1]==dic[1][1]:
        print(dic[1][0])
    else:
        print(dic[0][0])
else:
    print(dic[0][0])
print(m[-1]-m[0])
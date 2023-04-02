import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()

cnt = 0
i = 0
j =0
while i < m - 1:
    if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
        j += 1
        if j == n: 
            j -= 1 
            cnt += 1 
        i += 2  
        continue
    i += 1
    j = 0
print(cnt)
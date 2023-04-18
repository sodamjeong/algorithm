import sys
input = sys.stdin.readline

n = {}
cnt = 0

for _ in range(int(input())):
    m = input().strip()
    if m == 'ENTER':
        cnt += len(n)
        n.clear()
    else:
        if m not in n:
            n[m] = 1
        else:
            n[m] += 1
cnt += len(n)
print(cnt)
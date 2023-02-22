import sys
input = sys.stdin.readline

num = int(input())
n = [i for i in range(num,0,-1)]
m = [int(input()) for _ in range(num)]
stack = []
cnt = []
a = 0

while 1:
    for i in n:
        stack.append(n.pop())
        cnt.append('+')
        if stack[-1] == m[a]:
            while 1:
                stack.pop()
                cnt.append('-')
                a += 1
                if len(stack) == 0:
                    break
                elif stack[-1] != m[a]:
                    break
    if len(n) == 0:
        break
if len(stack) != 0:
    print('NO')
else:
    print(*cnt,sep='\n')
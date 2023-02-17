from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
for _ in range(int(input())):
    x = input().rstrip('\n')
    n = x[:5]
    if n == 'push ':
        queue.append(int(x[5:]))
    elif x == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif x == 'size':
        print(len(queue))
    elif x == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif x == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
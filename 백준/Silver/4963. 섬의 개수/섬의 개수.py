import sys
input = sys.stdin.readline

d = [(1,1),(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]

while True:
    w,h = map(int,input().split())
    if w == h == 0:
        break
    
    world = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if world[i][j]:
                stack = [(i,j)]
                world[i][j] = 0
                cnt += 1

                while stack:
                    x,y = stack.pop()
                    for a,b in d:
                        dx=x+a
                        dy=y+b
                        if h>dx>=0 and w>dy>=0 and world[dx][dy]:
                            stack.append((dx,dy))
                            world[dx][dy] = 0
    print(cnt)
n,m = map(int,input().split())
board = [list(input()) for i in range(n)]
color = []

for a in range(n-7):
    for b in range(m-7):
        cnt = 0
        for x in range(a,a+8):
            for y in range(b,b+8):
                if ((x+y) % 2 == 0 and board[x][y]=='W') or \
                ((x+y) % 2 == 1 and board[x][y]=='B'):
                    cnt += 1
        color.append(min(cnt,64-cnt))
print(min(color))
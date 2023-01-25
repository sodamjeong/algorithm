paper = [[0]*100 for _ in range(101)]

for i in range(int(input())):
    x,y = map(int,input().split())

    for n in range(x,x+10):
        for m in range(y,y+10):
            paper[n][m] = 1

size = 0 
for cnt in paper:
    size += cnt.count(1)
print(size)
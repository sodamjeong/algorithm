score = [[int(input()), i+1] for i in range(8)]
score = sorted(score, key = lambda x: -x[0])
num = []
cnt = 0

for i in range(5):
    cnt += score[i][0]
    num.append(score[i][1])
    
print(cnt)
for i in sorted(num):
    print(i, end = ' ')
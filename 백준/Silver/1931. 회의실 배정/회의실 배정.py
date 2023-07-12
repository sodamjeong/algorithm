meeting = [ list(map(int,input().split())) for _ in range(int(input()))]
meeting.sort(key=lambda x:(x[1],x[0]))

start, cnt = 0,0
for i in range(len(meeting)):
    if start <= meeting[i][0]:
        start = meeting[i][1]
        cnt += 1
print(cnt)
people = []
cnt = 0
for _ in range(4):
    a,b = map(int,input().split())
    cnt -= a
    people.append(cnt)
    cnt += b
    people.append(cnt)
print(max(people))
n = int(input())
m = list(map(int,input().split()))
up = []
road = 0
for i in range(n-1):
    if m[i] < m[i+1]:
        road += m[i+1] - m[i]
    else:
        up.append(road)
        road = 0
up.append(road)
print(max(up))
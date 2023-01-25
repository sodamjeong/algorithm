n,m = map(int,input().split())
card = list(map(int,input().split()))
ans = []

for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1,n):
            if card[x]+card[y]+card[z] <= m:
                ans.append(card[x]+card[y]+card[z])
print(max(ans))
n = int(input())
num = list(map(int, input().split()))
cnt = [0] * n
cnt[0] = num[0]

for i in range(1,n):
  cnt[i] = max(num[i], cnt[i-1]+num[i])
    
print(max(cnt))
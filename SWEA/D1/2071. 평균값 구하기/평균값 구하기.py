t = int(input())

for i in range(1,t+1):
    n = list(map(int,input().split()))
    print(f'#{i}', round(sum(n) / len(n)))
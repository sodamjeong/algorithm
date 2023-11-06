n = int(input())
home = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,len(home)):
  home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
  home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
  home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]

print(min(home[-1][0], home[-1][1], home[-1][2]))
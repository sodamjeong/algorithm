a = int(input())
word = [ input() for _ in range(a)]
ans = [ input() for _ in range(int(input()))]

if a > 1:
  if word[0] == '?':
    for i in ans:
      if i[-1] == word[1][0] and i not in word:
        print(i)
  elif word[-1] == '?':
    for i in ans:
      if i[0] == word[-2][-1] and i not in word:
        print(i)
  else:
    for i in range(a):
      if word[i] == '?':
        n,m = word[i-1][-1], word[i+1][0]
        for j in ans:
          if j[0] == n and j[-1] == m and j not in word:
            print(j)
else:
  print(ans[0])
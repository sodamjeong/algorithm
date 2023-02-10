n = ['a', 'e', 'i', 'o', 'u']
for t in range(1,int(input())+1):
    word = list(input())
    m = [i for i in word if i not in n]
    print(f'#{t}',''.join(m))
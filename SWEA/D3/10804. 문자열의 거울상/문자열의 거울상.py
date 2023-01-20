text = ['b','p','q','d']
mirror = text[::-1]

for i in range(1,int(input())+1):
    n = list(input()[::-1])
    m = [mirror[text.index(x)] for x in n]
    print(f'#{i} {"".join(m)}')
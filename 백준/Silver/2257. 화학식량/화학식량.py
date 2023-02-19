num = {'H':1, 'C':12, 'O':16}
lst = []
for i in input():
    if i == '(':
        lst.append(i)
    elif i ==')':
        cnt = 0
        while 1:
            n = lst.pop()
            if n == '(':
                break
            else:
                cnt += n
        lst.append(cnt)
    elif i in num:
        lst.append(num[i])
    else:
        lst[-1] *= int(i)
print(sum(lst))
n = input()
stick = n.replace('()','|')
cnt, result = 0, 0

for i in stick:
    if i == '(':
        cnt += 1
    elif i == ')':
        cnt -= 1
        result += 1
    else:
        result += cnt
print(result)
def star(n):
    lst = []
    if n == 1:
        lst.append('*')
    else:
        m = star(n//3)
        
        for i in m:
            lst.append(i*3)
        for i in m:
            lst.append(i+' '*(n//3)+i)
        for i in m:
            lst.append(i*3)
        
    return lst

print('\n'.join(star(int(input()))))
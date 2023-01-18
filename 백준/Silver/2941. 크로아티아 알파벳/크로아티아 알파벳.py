n = input()
m = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in m:
    n = n.replace(i,'1')
print(len(n))
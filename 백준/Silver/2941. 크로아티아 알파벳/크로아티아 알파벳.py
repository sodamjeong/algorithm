a = input()
b = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
n = 0
m = 2

x = a.replace('=','')
y = x.replace('-','')
z = 1

while m < (len(y) + 1):
    if y[n:m] not in b:
        z += 1
    n += 1
    m += 1

z -= a.count('dz=')

print(z)
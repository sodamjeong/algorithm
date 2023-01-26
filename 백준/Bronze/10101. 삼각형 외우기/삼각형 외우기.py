n = [int(input()) for i in range(3)]
m = ['Equilateral','Isosceles','Scalene']
if sum(n) != 180:
    print('Error')
else:
    print(m[len(set(n))-1])
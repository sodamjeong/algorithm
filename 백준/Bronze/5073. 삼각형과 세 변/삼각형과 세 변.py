import sys
input = sys.stdin.readline

while True:
  data = []
  x, y, z = map(int, input().split())
  if x == 0 and y == 0 and z == 0:
    break
  data.append(x)
  data.append(y)
  data.append(z)
  data.sort()

  if data[2] >= data[0] + data[1]:
    print('Invalid')
  else:
    if data[0] == data[1] and data[1] == data[2]:
      print('Equilateral')
    elif data[0] == data[1] and data[1] != data[2]:
      print('Isosceles')
    elif data[0] != data[1] and data[1] == data[2]:
      print('Isosceles')
    else:
      print('Scalene')
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
block = list(map(int,input().split()))
rain = 0
left, right = 0, m-1
l_b, r_b = block[left], block[right]

while(left < right):
  l_b, r_b = max(l_b, block[left]), max(r_b, block[right])

  if l_b <= r_b:
    rain += l_b - block[left]
    left += 1
  else:
    rain += r_b - block[right]
    right -= 1

print(rain)
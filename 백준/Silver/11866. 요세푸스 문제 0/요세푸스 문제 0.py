import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
people = deque([i for i in range(1,n+1)])
person = []

while people:
    people.rotate(-(k-1))
    person.append(people.popleft())
print(f'<{", ".join(map(str,person))}>')
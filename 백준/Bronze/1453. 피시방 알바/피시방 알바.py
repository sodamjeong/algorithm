people = int(input())
seat = list(map(int,input().split()))
seats = []

for i in seat:
    if i not in seats:
        seats.append(i)
print(people-len(seats))
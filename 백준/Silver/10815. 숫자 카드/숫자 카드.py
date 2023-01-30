input()
cards = {}
for i in list(map(int,(input().split()))):
    cards[i] = 1
input()
for i in list(map(int,input().split())):
    print(cards.get(i,0),end=" ")
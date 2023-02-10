for t in range(1,int(input())+1):
    num = int(input())
    cards = list(input().split())
    if num % 2 == 1:
        n = (num//2)+1
    else:
        n = num//2
    card1 = cards[:n]
    card2 = cards[n:]
    new_cards = []
    for i in range(n):
        try:
            new_cards.append(card1[i])
            new_cards.append(card2[i])
        except:
            pass
    print(f'#{t}',*new_cards)

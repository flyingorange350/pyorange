t=input()
t=int(t)
output = []
for _ in range(t):
    card_cnt = input()                      # card_cnt 전부 card_cnt로 바꿔야함 어떻게하더라 그거
    cards = list(map(int, input().split()))
    numlist = sorted(cards)
    gw = []
    while card_cnt > 0:
        numlist = sorted(cards)
        for i in range(card_cnt):
            if cards.index(numlist[len(numlist)-1]) != (card_cnt-1) - cards.index(numlist[len(numlist)-1]):
                if cards.index(numlist[len(numlist)-1]) % 2 != 0 and ((card_cnt-1) - cards.index(numlist[len(numlist)-1])) % 2 == 0:
                    gw.append(cards[0])
                    cards.remove(cards[0])
                elif cards.index(numlist[len(numlist)-1]) % 2 == 0 and ((card_cnt-1) - cards.index(numlist[len(numlist)-1])) % 2 != 0:
                    gw.append(cards[card_cnt-1])
                    cards.remove(cards[card_cnt-1])
                elif cards.index(numlist[len(numlist)-1]) % 2 == 0 and ((card_cnt-1) - cards.index(numlist[len(numlist)-1])) % 2 == 0 or cards.index(numlist[len(numlist)-1]) % 2 != 0 and ((card_cnt-1) - cards.index(numlist[len(numlist)-1])) % 2 != 0:
                    if cards[2] >= cards[1] and card_cnt-3 <= card_cnt-2:
                        gw.append(cards[0])
                        cards.remove(cards[0])
                    elif cards[2] <= cards[1] and card_cnt-3 >= card_cnt-2:
                        gw.append(cards[card_cnt-1])
                        cards.remove(cards[card_cnt-1])
                        
        for j in range(len(gw)):
            if j%2 != 0:
                gw.remove(gw[j])
    output.append(sum(gw))

for k in range(t-1):
    print(gw[k])

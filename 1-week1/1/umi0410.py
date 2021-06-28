# 숫자 카드 게임 ㅎㅅㅎ
length, numOfTurns = map(int, input().split())
cards = sorted([int(card) for card in input().split()])

for i in range(1, numOfTurns + 1):
    if i % 2 == 1:
        cards = cards[1:]
    else:
        cards = cards[:-1]

print(sum(cards))
# print(cards)
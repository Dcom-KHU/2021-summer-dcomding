# 숫자 카드 게임 ㅎㅅㅎ
length, numOfTurns = map(int, input().split())
cards = sorted([int(card) for card in input().split()])

# 굳이 이렇게 반복문을 돌릴 필요 없이
# for i in range(1, numOfTurns + 1):
#     if i % 2 == 1:
#         cards = cards[1:]
#     else:
#         cards = cards[:-1]

# 생각해보면 그냥 짤릴 앞 뒤는 정해져있으니
cards = cards[(numOfTurns+1)//2:length - numOfTurns//2]

print(sum(cards))

# print(cards)
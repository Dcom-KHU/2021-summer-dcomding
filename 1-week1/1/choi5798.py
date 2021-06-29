from collections import deque
n, k = list(map(int, input().split()))
cards = list(map(int, input().split()))
for i in range(1, k+1):
    cards = deque(sorted(cards))
    if i%2 == 0:
        temp = cards.pop()
    else:
        cards.popleft()
print(sum(cards))

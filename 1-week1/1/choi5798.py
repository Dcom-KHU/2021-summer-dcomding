from collections import deque
n, k = list(map(int, input().split()))
cards = list(map(int, input().split()))
cards = deque(sorted(cards))
for i in range(1, k+1):
    if i%2 == 0:
        temp = cards.pop()
    else:
        cards.popleft()
print(sum(cards))

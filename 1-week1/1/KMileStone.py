n, k = map(int, input().split())
card = list(map(int, input().split()))


# sort card
card.sort()

# remove card by rule
for iter in range(k):
    if iter % 2 == 0:
        card.pop(0)
    else:
        card.pop()

# sum remaining card
print(sum(card))

n, k = input("").split()
n = int(n)
k = int(k)
cards = input("").split()
cards.sort()
l = len(cards)
for i in range(l):
    cards[i] = int(cards[i])
t = 1
if k < n:
    while(t <= k):
        if t%2 == 1:
            del cards[0]
        else:
            del cards[-1]
        t += 1
else:
    print(0)

result = 0
for card in cards:
    result += card

print(result)
n, k = input("").split()
n = int(n)
k = int(k)
cards = input("").split()
for i in range(n):
    cards[i] = int(cards[i])
cards.sort()
t = 1 #turns
if k < n:
    while(t <= k):
        if t%2 == 1:
            del cards[0]
        else:
            del cards[-1]
        t += 1

    result = 0
    
    for card in cards:
        result += card
        
    print(result)
    
else:
    print(0)
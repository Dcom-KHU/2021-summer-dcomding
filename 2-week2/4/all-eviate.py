n = int(input(""))
apples = []
for i in range(n):
    apples.append(input(""))

products = set(apples) # total apple products
np = len(products)

optimum = -1

basket = {}
basketset = set()

start = 0
end = 0

buyfrom = 0
buyto = 0

counts = 0

for start in range(n):
    done = False

    for end in range(counts, n):
        try:
            basket[apples[end]] += 1
        except:
            basket[apples[end]] = 1
            basketset.add(apples[end])

        if np == len(basketset):
            if optimum < 0 or (end - start) < optimum:
                optimum = end - start
                buyfrom = start + 1
                buyto = end + 1
            
            done = True
            counts = end
            break
    if not done:
        break

    if apples[start] in basket.keys():
        if basket[apples[start]] == 1:
            del basket[apples[start]]
            basketset.remove(apples[start])
        else:
            basket[apples[start]] -= 1
    
    if apples[end] in basket.keys():
        if basket[apples[end]] == 1:
            del basket[apples[end]]
            basketset.remove(apples[end])
        else:
            basket[apples[end]] -= 1

print(buyfrom)
print(buyto)
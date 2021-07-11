n = int(input(""))
apples = []
for i in range(n):
    apples.append(input(""))

products = len(set(apples)) # total apple products

buyfrom = 0
buyto = 0

for counts in range(products, n):
    if buyfrom != 0 and buyto != 0:
        break
    basket = []
    for start in range(0, n-products+1):
        end = start + counts
        basket = apples[start:end]
        basketset = set(basket)
        if len(basketset) == products:
            buyfrom = start + 1
            buyto = end
            break

print(buyfrom)
print(buyto)
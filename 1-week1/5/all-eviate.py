n = int(input(""))
money = list(map(int, input("").split()))
steal1 = [0 for i in range(n)]
steal2 = [0 for i in range(n)]

#first included
steal1[0] = steal1[1] = money[0]
for i in range(2, n):
    steal1[i] = max(steal1[i-1], steal1[i-2] + money[i])

#first excluded
steal2[0] = 0
steal2[1] = money[1]
for i in range(2, n):
    steal2[i] = max(steal2[i-1], steal2[i-2] + money[i])

print(max(steal1[-2], steal2[-1]))
n, k = map(int, input("").split())
stones = input("").split()
for i in range(n):
    stones[i] = int(stones[i])

m = 0 #members
able = True

while able:
    skip = 0
    j = 0
    for j in range(n):
        if stones[j] == 0:
            skip += 1
            if skip >= k:
                able = False
                break
        else:
            stones[j] -= 1
            skip = 0
    if skip < k:
        m += 1

print(m)
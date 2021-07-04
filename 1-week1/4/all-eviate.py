n, k = map(int, input("").split())
stones = input("").split()
for i in range(n):
    stones[i] = int(stones[i])

m = 0 #members
mn = min(stones)
mx = max(stones)
able = True

while mn <= mx:
    md = (mn + mx)//2
    skip = 0
    mdv = True
    for i in range(n):
        if stones[i] < md:
            skip += 1
            if skip >= k:
                mdv = False
                break
        else:
            skip = 0
    if mdv:
        m = md
        mn = md + 1
    else:
        mx = md - 1

print(m)
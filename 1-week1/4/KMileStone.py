n, k = map(int, input().split())
stones = list(map(int, input().split()))


# if k == n, success member is max(stones)
# if k == 1, success member is min(stones)
max_stone = max(stones)
min_stone = min(stones)

count = 0
member = max_stone

for i in range(max_stone, min_stone-1, -1):
    count = 0
    valid = True

    for stone in stones:
        # if stone < member, stone will be zero
        if stone < i:
            count += 1
        else:
            count = 0

        # if k zeros in a row, you should jump k+1
        if count >= k:
            valid = False
            break

    # success member
    if valid == True:
        member = i
        break

print(member)

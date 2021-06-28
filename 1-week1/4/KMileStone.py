n, k = map(int, input().split())
stones = list(map(int, input().split()))


# if k == 1, success member is min(stones)
# if k == n, success member is max(stones)
left = min(stones)
right = max(stones)
count = 0
member = right

# binary search
while left <= right:
    mid = (left + right) // 2
    count = 0
    valid = True

    # check mid member
    for stone in stones:
        # if stone < member, stone will be zero before passing
        if stone < mid:
            count += 1
        else:
            count = 0

        # fail : if k zeros in a row, you should jump k+1
        # should check less member
        if count >= k:
            valid = False
            right = mid-1
            break

    # success
    # should check more member
    if valid == True:
        member = mid
        left = mid+1

print(member)

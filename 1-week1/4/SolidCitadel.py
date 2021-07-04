n, k = map(int, input().split())
stones = list(map(int, input().split()))

left, right = 1, 2*10**8
while left <= right:
    mid = (left+right)//2
    count = k
    for s in stones:
        if s <= mid:
            count -= 1
        else:
            count = k
        if not count:
            break
    if count:
        left = mid + 1
    else:
        right = mid - 1
    
print(left)

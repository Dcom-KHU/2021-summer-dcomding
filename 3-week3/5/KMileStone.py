n = int(input())
heights = list(map(int, input().split()))


area = 0
max_area = 0

# binary search
left = min(heights)
right = max(heights)

while left <= right:
    area = 0
    updated = False
    mid = (left + right) // 2

    for h in heights:
        # if mid <= h, you can make rectangle
        if mid <= h:
            area += mid
        else:
            # update max
            if area > max_area:
                max_area = area
                updated = True

            area = 0

    # update max with last rectangle
    if area > max_area:
        max_area = area
        updated = True

    # if updated, check higher height
    if updated:
        left = mid + 1

    # if not updated, check lower height
    else:
        right = mid - 1

print(max_area)

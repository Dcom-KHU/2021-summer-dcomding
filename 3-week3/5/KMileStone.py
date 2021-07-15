n = int(input())
heights = list(map(int, input().split()))


# divide with min
def divide(seq):
    global max_area
    mid = min(seq)
    idx = seq.index(mid)
    area = 0

    for h in heights:
        # if mid <= h, you can make rectangle
        if mid <= h:
            area += mid
        else:
            # update max
            if area > max_area:
                max_area = area

            area = 0

    # update max with last rectangle
    if area > max_area:
        max_area = area

    # divide more
    left = seq[:idx]
    right = seq[idx+1:]
    if len(left) > 0:
        divide(left)
    if len(right) > 0:
        divide(right)


max_area = 0
divide(heights)

print(max_area)

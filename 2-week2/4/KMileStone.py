n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)


# num of item class
n_item = len(set(items))

min = 0
max = n-1
left = 0
right = n_item-1
prev = 0
n_sliced = len(set(items[left:right+1]))

while right < n:

    # if included all item
    if n_sliced == n_item:
        # update min max
        if right - left < max - min:
            min = left
            max = right
            if max - min + 1 == n_item:
                break

        # take less item
        prev = left
        left += 1
        while left <= right and items[left] == items[left+1]:
            left += 1
        if items[prev] not in items[left:right+1]:
            n_sliced -= 1

    # if not included all item
    else:
        # take more item
        prev = right
        while right < n-1 and items[right] == items[right+1]:
            right += 1
        right += 1
        if right < n and items[right] not in items[left:prev+1]:
            n_sliced += 1

# num of stand starts with 1
min += 1
max += 1

print(min)
print(max)

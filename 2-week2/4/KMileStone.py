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

while right < n:
    # if included all item
    if len(set(items[left:right+1])) == n_item:
        # update min max
        if right - left < max - min:
            min = left
            max = right

        # take less item
        left += 1

    # if not included all item
    else:
        # take more item
        right += 1

# num of stand starts with 1
min += 1
max += 1

print(min)
print(max)

n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)


min = 0
max = n - 1
n_item = len(set(items))
left = 0
right = n_item - 1
count = {}
for i in items[left:right + 1]:
    count.setdefault(i, 0)
    count[i] += 1
while right < n - 1 and len(count) != n_item:
    right += 1
    count.setdefault(items[right], 0)
    count[items[right]] += 1

while right < n:
    # if included all item
    if len(count) == n_item:
        # update min max
        if right - left < max - min:
            min = left
            max = right
            if max - min + 1 == n_item:
                break

        # shorten window
        count[items[left]] -= 1
        if not count[items[left]]:
            del count[items[left]]
        left += 1

    # if not included all item
    else:
        # slide window right
        right += 1
        if right < n:
            count.setdefault(items[right], 0)
            count[items[right]] += 1
        count[items[left]] -= 1
        if not count[items[left]]:
            del count[items[left]]
        left += 1


# num of stand starts with 1
min += 1
max += 1

print(min)
print(max)

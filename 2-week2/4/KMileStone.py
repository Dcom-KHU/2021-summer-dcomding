n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)


min = 0
max = n-1
count = {i:0 for i in set(items)}
left = 0
right = len(count.keys())-1
for i in items[left:right+1]:
    count[i] += 1
while right < n-1 and 0 in count.values():
    right += 1
    count[items[right]] += 1

while right < n:
    # if included all item
    if 0 not in count.values():
        # update min max
        if right - left < max - min:
            min = left
            max = right
            if max - min + 1 == len(count.keys()):
                break

        # shorten window
        count[items[left]] -= 1
        left += 1

    # if not included all item
    else:
        # slide window right
        right += 1
        if right < n:
            count[items[right]] += 1
        count[items[left]] -= 1
        left += 1


# num of stand starts with 1
min += 1
max += 1

print(min)
print(max)

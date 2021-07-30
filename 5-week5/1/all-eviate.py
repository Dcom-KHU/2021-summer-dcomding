s = input()
l = []
l.extend(s)

areas = [0, 0]

cur = None

for i in range(len(s)):
    if l[i] != cur:
        cur = l[i]
        areas[int(l[i])] += 1

print(min(areas[0], areas[1]))
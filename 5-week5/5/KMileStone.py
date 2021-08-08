n = int(input())
words = []
for i in range(n):
    words.append(input())


# tree : root - h - e - l - l - o - '\0'
#                             - '\0'
#                     - a - v - e - n - '\0'
#             - g - o - o - d - b - y - e - '\0'
root = {}
cursor = root

# make dictionary
for word in words:
    cursor = root

    for c in word+'\0':
        node = cursor.get(c)

        # if not found, make new node
        if not node:
            node = {}
            cursor[c] = node

        cursor = node


# count input char
if len(root) == 1:
    count = [1 for i in range(n)]
else:
    count = [0 for i in range(n)]

for i in range(n):
    cursor = root

    for c in words[i]:
        # if more than 1 child exist, you should choose char
        if len(cursor) > 1:
            count[i] += 1

        cursor = cursor.get(c)


for e in count:
    print(e)
n = int(input())
words = []
for i in range(n):
    words.append(input())


# tree
class Node:
    def __init__(self, val):
        self.val = val
        self.child = []


# tree : head - h - e - l - l - o - '\0'
#                             - '\0'
#                     - a - v - e - n - '\0'
#             - g - o - o - d - b - y - e - '\0'
head = Node('head')
cursor = head
found = False

# make dictionary
for word in words:
    cursor = head

    for c in word+'\0':
        # find char from child
        for node in cursor.child:
            if node.val == c:
                cursor = node
                found = True
                break

        # if not found, make new node
        if not found:
            node = Node(c)
            cursor.child.append(node)
            cursor = node
        else:
            found = False

# count input char
if len(head.child) == 1:
    count = [1 for i in range(n)]
else:
    count = [0 for i in range(n)]

for i in range(n):
    cursor = head

    for c in words[i]:
        # if more than 1 child exist, you should choose char
        if len(cursor.child) > 1:
            count[i] += 1

            # find char from child
            for node in cursor.child:
                if node.val == c:
                    cursor = node
                    break

        # else, auto
        else:
            cursor = cursor.child[0]


for e in count:
    print(e)

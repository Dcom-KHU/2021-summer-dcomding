n, f, k = map(int, input().split())
cmd = []
for i in range(k):
    cmd.append(input())


# double linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self
        self.next = self

    def add(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        del self


head = Node('head')
cursor = head
for i in range(n):
    cursor.add(Node(i))
    cursor = cursor.next

cursor = head
for i in range(f+1):
    cursor = cursor.next

undo = []

for c in cmd:
    if c[0] == 'U':
        for i in range(int(c[2:])):
            cursor = cursor.prev

    elif c[0] == 'D':
        for i in range(int(c[2:])):
            cursor = cursor.next

    elif c[0] == 'C':
        temp = cursor

        # if tail
        if cursor.next == head:
            cursor = cursor.prev
        else:
            cursor = cursor.next

        undo.append((temp.prev, temp.val))

        temp.delete()

    elif c[0] == 'Z':
        (node, val) = undo.pop()
        node.add(Node(val))


undo.sort(key=lambda x: x[1])
for e in undo:
    print(e[1])

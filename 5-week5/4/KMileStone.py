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


# list : head <=> 0 <=> 1 <=> ...
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

        undo.append(temp)
        temp.delete()

    elif c[0] == 'Z':
        node = undo.pop()

        # node contains its previous node just before delete
        node.prev.add(node)


undo.sort(key=lambda x: x.val)
for node in undo:
    print(node.val)

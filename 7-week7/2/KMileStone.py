str = list(input())


# double linked list
class Node:
    def __init__(self, char=''):
        self.char = char
        self.next = None
        self.prev = None

    def add(self, char):
        node = Node(char)
        node.prev = self
        node.next = self.next
        if self.next:
            self.next.prev = node
        self.next = node

    def delete(self):
        self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        del self

head = Node('head')
cursor = head

for c in str:
    if c == '<':
        if cursor.char != 'head':
            cursor = cursor.prev
    elif c == '>':
        if cursor.next:
            cursor = cursor.next
    elif c == '-':
        if cursor.char != 'head':
            temp = cursor
            cursor = cursor.prev
            temp.delete()
    else:
        cursor.add(c)
        cursor = cursor.next


cursor = head.next
while cursor:
    print(cursor.char, end='')
    cursor = cursor.next

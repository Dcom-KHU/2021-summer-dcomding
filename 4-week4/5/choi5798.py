from collections import deque
n = int(input())
values = list(map(int, input().split()))
c = 0

class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0

def insert(x, n):
    global c
    c+=1
    if x < n.value:
        if n.left == None:
            child = node()
            child.value = x
            n.left = child
        else:
            insert(x, n.left)
    else:
        if n.right == None:
            child = node()
            child.value = x
            n.right = child
        else:
            insert(x, n.right)
tree = node()
tree.value = values[0]
print(c)
for v in range(1, n):
    insert(values[v], tree)
    print(c)
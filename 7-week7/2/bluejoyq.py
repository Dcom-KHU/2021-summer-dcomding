# linked list

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
def solve():
    values = input()
    
    # data, left, right
    root = Node(None)
    cur = root
    # 커서왼쪽이 현재
    for value in values:
        if value == "<":
            if cur.left == None:
                continue
            cur = cur.left
        elif value == ">":
            if cur.right == None:
                continue
            cur = cur.right
        elif value == "-":
            if cur.value == None:
                continue
            if cur.left != None:
                cur.left.right = cur.right
            if cur.right != None:
                cur.right.left = cur.left
            tmp = cur
            cur = cur.left
            del tmp

        else:
            node = Node(value)
            node.left = cur
            node.right = cur.right
            cur.right = node
            cur = node
    result = ""
    try:
        cur = root.right
        while cur.value != None:
            result += cur.value
            cur = cur.right
    except:
        pass
    print(result)
solve()
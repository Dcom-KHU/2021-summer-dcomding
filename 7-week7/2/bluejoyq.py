# linked list

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
def solve():
    values = input()
    
    # data, left, right
    start = Node(None)
    end = Node(None)
    start.right = end
    end.left = start
    
    cur = start
    # 커서왼쪽이 현재
    for value in values:
        if value == "<":
            if cur == start:
                continue
            cur = cur.left
        elif value == ">":
            if cur == end:
                continue
            cur = cur.right
        elif value == "-":
            if cur == start:
                continue
            cur.left.right = cur.right
            if cur.right != None:
                cur.right.left = cur.left
            tmp = cur
            cur = cur.left
            if tmp != end:
                del tmp

        else:
            node = Node(value)
            node.left = cur
            node.right = cur.right
            cur.right = node
            cur = node
    result = ""
    try:
        cur = start.right
        while cur != end:
            result += cur.value
            cur = cur.right
    except:
        pass
    print(result)
solve()
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# 대충 이런느낌?

N = int(input())
values = list(map(int, input().split()))
def insert(val , node):
    #print(val,node)
    
    if val < node.value:
        if node.left == None:
            node.left = Node(val)
        else:
            return insert(val, node.left) + 1
    else:
        if node.right == None:
            node.right = Node(val)
        else:
            return insert(val, node.right) + 1
    return 1
root = Node(values[0])
result = ""
num = 0
for value in values[1:]:
    num += insert(value, root)
    result += str(num) + "\n"
print(0)
print(result)
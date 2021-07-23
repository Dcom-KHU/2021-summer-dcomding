import sys
input = sys.stdin.readline
# 참고글 : https://www.crocus.co.kr/641
# 참고글 : https://lsh424.tistory.com/73
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.color = 'Red'
        
        
import time
import math
def logging_time(original_fn):
    
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, round(end_time-start_time, 7)))
        return result
    return wrapper_fn

class RedBlackTree:
    def __init__(self):
        self.root = None
    
    def find_gp_node(self,node):
        if node == None or node.parent == None:
            return None
        return node.parent.parent
    
    def find_uncle_node(self,node):
        grandparent_node = self.find_gp_node(node)
        if grandparent_node == None:
            return None
    
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
        
    def rotate_left(self,node):
        c = node.right
        p = node.parent
        # node와 c 위치 변경
        if (c.left != None):
            c.left.parent = node
    
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
        # 만약 변경해 올라간 위치가 root라면
        if c.parent == None:
            self.root = c
        # 아니라면 node의 원래 위치에 c 등록
        else:
            if p.left == node:
                p.left = c
            else:
                p.right = c
                
    def rotate_right(self,node):
        c = node.left
        p = node.parent
    
        if (c.right != None):
            c.right.parent = node
    
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
        else:
            if (p.right == node):
                p.right = c
            else:
                p.left = c
    
    # case1. 루트 노드는 항상 블랙  
    def insert_case1(self,node):
        if node.parent == None:
            node.color = 'Black'
        else:
            self.insert_case2(node)
            
    # case2. 부모 노드가 블랙이면 회전, 색변환등 수행 필요 x, 하지만 빨강색이라면 case3 수행
    def insert_case2(self,node):
        if node.parent.color == 'Black':
            return
        else:
            self.insert_case3(node)
    
    # case3. 부모노드, 삼촌노드 모두 빨강이라면 색변환 수행, 아닐경우 case4로 이동
    def insert_case3(self,node):
        uncle = self.find_uncle_node(node)
        while uncle != None and uncle.color == 'Red':
            grandparent = uncle.parent
            grandparent.color = 'Red'
            grandparent.left.color = 'Black'
            grandparent.right.color = 'Black'
            uncle = self.find_uncle_node(grandparent)
            if uncle.parent == None:
                return 
        if uncle and uncle.parent:      
            self.insert_case4(node)
            
    # case4,5 회전 수행
    def insert_case4(self,node):
        
        grandparent = self.find_gp_node(node)
    
        if(node == node.parent.right and node.parent == grandparent.left):
            self.rotate_left(node.parent)
            node = node.left
        elif (node == node.parent.left and node.parent == grandparent.right):
            self.rotate_right(node.parent)
            node = node.right
    
        node.parent.color = 'Black'
        grandparent.color = 'Red'

        if (node == node.parent.left):
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent) 
        
    # 삽입
    def insert(self, data):
        node, bigger_min, smaller_max = self.insert_value(data)
        self.insert_case1(node)
        return bigger_min, smaller_max
    # 재귀에서 while로 바꾸고 항상 한개의 데이터만 입력받게 바꿈.
    def insert_value(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root, None, None
        node = self.root
        parent_node = None
        smaller_max = None
        bigger_min = None
        # min max 안달아도 될 것 같긴함.
        while node != None:
            parent_node = node
            if data < node.data:
                bigger_min = node.data
                node = node.left
            else:
                smaller_max = node.data
                node = node.right
        node = Node(data)
        node.parent = parent_node
        if data < parent_node.data:
            parent_node.left = node
        else:
            parent_node.right = node
            
        return node, bigger_min, smaller_max

class BinaryNode:
    def __init__(self, depth):
        self.depth = depth
        self.right = self.left = None
'''
def check(node):
    if not node.left  == None : check(node.left)
    if node.parent != None:
        print('key: ', node.data, 'parents: ', node.parent.data, 'color: ', node.color, end = '\n')
    else:
        print('key: ', node.data, 'parents: ', node.parent, 'color: ', node.color, end = '\n')
    if not node.right == None : check(node.right)
'''
def solve():
    N = int(input())
    values = list(map(int, input().split()))
    rb_tree = RedBlackTree()
    tree = [0] * (N + 1)
    result_str = ""
    result = 0
    for value in values:
        bigger_min, smaller_max = rb_tree.insert(value)
        depth = 1
        try:
            if tree[bigger_min].left == None:
                tree[bigger_min].left = value
                depth = tree[bigger_min].depth + 1
        except:   
            pass
        
        try:
            if tree[smaller_max].right == None:
                tree[smaller_max].right = value
                depth = tree[smaller_max].depth + 1
        except:   
            pass

        tree[value] = BinaryNode(depth)
        result += depth - 1
        result_str += str(result) + '\n'
    print(result_str)
solve()
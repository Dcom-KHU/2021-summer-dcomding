import sys
input = sys.stdin.readline
class Tree:
    def __init__(self):
        self.nxt = {}
    
def solution():
    n = int(input())
    words = [0] * n
    root = Tree()
    for i in range(n):
        words[i] = input().rstrip()
        cur = root
        for char in words[i]:
            try:
                cur =  cur.nxt[char]
            except:
                cur.nxt[char] = Tree()
                cur = cur.nxt[char]
        cur.nxt[""] = Tree()
    
    
    result = ""
    for i in range(n):
        count = 0
        cur = root
        for char in words[i]:
            if len(cur.nxt) != 1:
                count += 1
            cur =  cur.nxt[char]
        
        result += str(count) + "\n"
    
    print(result)
solution()
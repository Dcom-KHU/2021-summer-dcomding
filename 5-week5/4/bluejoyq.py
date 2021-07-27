import sys
input = sys.stdin.readline
class Node:
    def __init__(self,idx):
        self.idx = idx
        self.bef = None
        self.nxt = None
        
def solution():
    n,f,k = map(int, input().split())
    
    # linked list 초기화
    values = [Node(i) for i in range(n)] 
    for i in range(n):
        try:
            values[i].nxt = values[i + 1]
        except:
            pass
        try:
            values[i+1].bef = values[i]
        except:
            pass
        
    deleted = [] # stk
    cur = values[f]
    
    for i in range(k):
        comm = list(input().split())
        
        if comm[0] == "U":
            for _ in range(int(comm[1])):
                cur = cur.bef
        elif comm[0] == "D":
            for _ in range(int(comm[1])):
                cur = cur.nxt
        elif comm[0] == "C":
            deleted.append(cur.idx)
            cur.idx = -1
            try:
                cur.bef.nxt = cur.nxt
            except:
                pass
            try:
                cur.nxt.bef = cur.bef
                cur = cur.nxt
            except:
                # 마지막이라서 nxt가 없다면
                cur = cur.bef
            
        else:
            restore = deleted.pop()
            target = values[restore]
            target.idx = restore
            nxt = target.nxt
            try:
                while nxt.idx == -1:
                    nxt = target.nxt
                
                if nxt.bef != None:
                    nxt.bef.nxt = target
                target.bef = nxt.bef
                nxt.bef = target
                target.nxt = nxt
                
                
            except:
                bef = target.bef
                while bef.idx == -1:
                    bef = target.bef
                
                if bef.nxt != None:
                    bef.nxt.bef = target
                target.nxt = bef.nxt
                bef.nxt = target
                target.bef = bef
                pass
    deleted.sort()
    print(*deleted)
            
solution()
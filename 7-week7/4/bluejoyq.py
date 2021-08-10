def solve():
    N = int(input())
    target = input().rstrip() 
    
    root = {}
    for i in range(N):
        chars = list(input())
        cur = root
        for char in chars:
            try:
                cur[char]
            except:
                cur[char] = {}
            cur = cur[char] 
        
    M = len(target)
    i = 0
    result = 0
    print(root)
    while i < M:
        cur = root.get(target[i])
        if cur == None:
            return -1
        while cur != None:
            i += 1
            try:
                cur = cur.get(target[i])
            except:
                return result + 1
        result += 1
    return result        
print(solve())
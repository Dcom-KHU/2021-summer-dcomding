import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    words = [0] * n
    root = {}
    root[""] = 0
    for i in range(n):
        words[i] = input().rstrip()
        cur = root
        for char in words[i]:
            try:
                cur =  cur[char]
            except:
                cur[char] = {}
                cur = cur[char]
        cur[""] = 0
    
    result = ""
    for i in range(n):
        count = 0
        cur = root
        for char in words[i]:
            if len(cur) != 1:
                count += 1
            cur =  cur[char]
        
        result += str(count) + "\n"
    
    print(result)

solution()
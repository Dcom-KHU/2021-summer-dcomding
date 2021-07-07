import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    values = [0] * n
    count_dict = {}
    for i in range(n):
        data = input().rstrip()
        values[i] = data
        count_dict[data] = 0
     
    goal= len(count_dict)
    
    
    def check():
        for i in count_dict.values():
            if not i:
                return False
        return True
        
    left = 0
    result = 0
    for right in range(n): 
        count_dict[values[right]] += 1
        if result:
            count_dict[values[left]] -= 1
            left += 1
        while check():
            result = [left + 1, right + 1]
            count_dict[values[left]] -= 1
            left += 1
    a,b = result
    print(a)
    print(b)
solution()
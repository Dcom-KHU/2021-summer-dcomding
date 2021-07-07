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
        if goal == len(count_dict):
            return True
        return False
    
    left = 0
    result = 0
    for right in range(n): 
        try:
            count_dict[values[right]] += 1
        except:
            count_dict[values[right]] = 1
        if result:
            count_dict[values[left]] -= 1
            if not count_dict[values[left]]:
                del count_dict[values[left]]
            left += 1
            
        while check():
            result = [left + 1, right + 1]
            count_dict[values[left]] -= 1
            if not count_dict[values[left]]:
                del count_dict[values[left]]
            left += 1
            
    a,b = result
    print(a)
    print(b)
solution()


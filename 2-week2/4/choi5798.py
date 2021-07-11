def solution(gems):
    answer = []
    kinds = set(gems)
    kinds_length = len(kinds)
    start = 0
    end = 0
    minimum_length = 99999999
    target_count = {}
    while end < len(gems):
        if target_count.get(gems[end]) is None:
            target_count[gems[end]] = 1
        else:
            target_count[gems[end]] += 1 
        
        if kinds_length == len(target_count.keys()):
            while start <= end:
                if target_count[gems[start]] > 1: # ==1이면 start가 넘어갈 때 target에서 무조건 빠지니까
                    target_count[gems[start]] -= 1
                    start += 1
                elif minimum_length > end - start:
                    answer = [start+1, end+1]
                    minimum_length = end - start
                    break
                else:
                    break
        end += 1
    return answer
n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)
beg, end = solution(items)
print(beg)
print(end)
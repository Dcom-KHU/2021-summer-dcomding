from collections import deque
def solution(gems):
    answer = []
    kinds = set(gems)
    start = 0
    target = deque()
    for end in range(len(gems)):
        target.append(gems[end])
        if kinds == set(target):
            while True:
                start += 1
                target.popleft()
                if start>end:
                    answer = [start, start]
                    return answer
                if kinds != set(target):
                    # if not answer:
                    answer = [start, end+1]
                    break
                    
        if answer:
            start += 1
            target.popleft()
                        
    return answer
n = int(input())
items = []
for i in range(n):
    item = input()
    items.append(item)
beg, end = solution(items)
print(beg)
print(end)
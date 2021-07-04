from collections import deque

def solution():
    s = deque(input())
    n = len(s)
    answer = 0
    for i in range(n):
        check = []
        couples = {"(":")", "[": "]","{":"}" }
        is_valid = True
        for j in range(n):
            cur = s[j]
            if cur in ("(","[","{"):
                check.append(cur)
            else:
                try:
                    if couples[check[-1]] == cur:
                        check.pop()
                    else:
                        raise()
                except:
                    is_valid = False
                    break
        if is_valid:
            answer += 1
        s.append(s.popleft())
    
    
    return answer
print(solution())
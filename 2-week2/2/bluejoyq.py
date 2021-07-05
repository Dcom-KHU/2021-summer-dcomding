from collections import deque

def solution():
    s = deque(input())
    n = len(s)
    answer = 0
    for i in range(n):
        check = []
        couples = {"(":")", "[": "]","{":"}" }
        is_valid = True
        
        # 올바른 괄호인지 체크한다.
        for j in range(n):
            cur = s[j]
            if cur in ("(","[","{"):
                check.append(cur)
                continue
            try:
                # 반대편 괄호가 들어올 경우 항상 stack의 최상단과 짝이 맞야아 한다.
                if couples[check.pop()] != cur:
                    raise()
            except:
                is_valid = False
                break
        if is_valid and not len(check):
            answer += 1
        s.append(s.popleft())
        
    return answer
print(solution())
#2주차-2
#괄호 회전하기
from collections import deque
def solution(ip):
    def check(s):
        stack=[]
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if c==")" and x!="(":
                    return False
                elif c=="]" and x!="[":
                    return False
                elif c=="}" and x!="{":
                    return False
        return len(stack)==0
    ip=deque(ip)
    answer=0
    for x in range(len(ip)):
        ip.rotate(-1)
        if check(ip):
            answer+=1
    return answer
#Review)deque 기능 제대로 알아보자!
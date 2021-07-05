# 문제 속에 답이 있다. 굳이 올바른 문자열 A와 B를 예시로 설명해준 이유가 있을 터.
# 이를 이용해 풀어보자.
# => 별로 문제 속에 답이 없네 ㅋㅋ....
# 스택 안 쓰면 {()}[] 이런건 못품.
def solution(s):
    answer = 0
    for i in range(len(s)):
        brace = s[i:] + s[:i]
        is_answer = verify(brace)
        if is_answer: answer += 1

    return answer

correct_braces = ("()", "[]", "{}")

def verify(brace:str):
    if len(brace) == 0:
        return True
    stack = []
    for i in range(0, len(brace)):
        if brace[i] in ('(', '{', '['):
            stack.append(brace[i])
        elif brace[i] in (')', '}', ']'):
            if len(stack) == 0:
                return False
            if (brace[i] == ')' and stack[-1] == '(') or \
                    (brace[i] == '}' and stack[-1] == '{') or \
                    (brace[i] == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False

    return len(stack) == 0


# print(verify("()"))
# print(verify("() (())()()[({[]})]"))
print(solution(input()))
# print(solution("]][["))

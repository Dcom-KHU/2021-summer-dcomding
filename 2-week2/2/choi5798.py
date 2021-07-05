s = input()
def solution(s):
    def rotate(s, x):
        return s[x:]+s[:x]
    def check(s):
        if len(s)%2 != 0:
            return False
        stack = []
        last_open = ''
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack:
                top = stack.pop()
                if (ch == ')' and top == '(') or (ch == '}' and top == '{') or (ch == ']' and top == '['):
                    continue
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True

    answer = 0
    for x in range(len(s)):
        rotated_s = rotate(s, x)
        if check(rotated_s):
            answer+=1
    return answer
print(solution(s))
def isRight(s):
    stack = list()
    for ch in s:
        for open, close in zip('[({', '])}'):
            if ch == open:
                stack.append(open)
                break
            elif ch == close:
                if stack and stack[-1] == open:
                    stack.pop()
                    break
                else:
                    return False
    return False if stack else True

s = input()
print(sum([isRight(s[i:]+s[:i]) for i in range(len(s))]))

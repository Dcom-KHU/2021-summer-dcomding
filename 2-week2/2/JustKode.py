def check_bracket(string):
    stack = []
    for e in string:
        if e in '[({':
            if len(stack) == 0 or stack[-1] in '[({':
                stack.append(e)
            else:
                return 0
        elif e == ']':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '[':
                return 0
            else:
                stack.pop()
        elif e == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '(':
                return 0
            else:
                stack.pop()
        elif e == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '{':
                return 0
            else:
                stack.pop()
    if len(stack) != 0:
        return 0
    
    return 1

string = input()
result = 0
for i in range(len(string)):
    result += check_bracket(string)
    string = string[1:] + string[0]

print(result)
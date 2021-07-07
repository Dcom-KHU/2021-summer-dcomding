def findClose(s, key):
    count = 0
    for i in range(len(s)):
        if s[i] == key[0]:
            count += 1
        elif s[i] == key[1]:
            count -= 1
            if count == 0:
                return i
    return -1
        
def isRight(s):
    if len(s):
        for key in ['[]', '()', '{}']:
            if s[0] == key[0]:
                close = findClose(s, key)
                if close != -1:
                    return isRight(s[1:close]) and isRight(s[close+1:])
    else:
        return True
    return False

s = input()
print(sum([isRight(s[i:]+s[:i]) for i in range(len(s))]))

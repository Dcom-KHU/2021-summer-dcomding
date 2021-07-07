def isRight(s):
    if len(s):
        for key in ['[]', '()', '{}']:
            if s[0] == key[0]:
                count = 0
                for i in range(len(s)):
                    if s[i] == key[0]:
                        count += 1
                    elif s[i] == key[1]:
                        count -= 1
                        if count == 0:
                            return isRight(s[1:i]) and isRight(s[i+1:])
    else:
        return True
    return False

s = input()
num = 0
for i in range(len(s)):
    if isRight(s[i:]+s[:i]):
        num += 1
print(num)

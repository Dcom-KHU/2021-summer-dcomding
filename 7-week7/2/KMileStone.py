str = list(input())


password = []
cursor = 0

for c in str:
    if c == '<':
        if cursor > 0:
            cursor -= 1
    elif c == '>':
        if cursor < len(password):
            cursor += 1
    elif c == '-':
        if cursor > 0:
            del password[cursor-1]
            cursor -= 1
    else:
        password.insert(cursor, c)
        cursor += 1


print(''.join(password))

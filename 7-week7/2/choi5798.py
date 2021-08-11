string = input()
password = []
cur = 0
for ch in string:
    if ch == '<':
        cur -= 1 if cur > 0 else 0
    elif ch == '>':
        cur += 1 if cur < len(password) else 0
    elif ch == '-':
        if cur != 0:
            del password[cur-1]
            cur -= 1
    else:
        password.insert(cur, ch)
        cur += 1
print(''.join(password))

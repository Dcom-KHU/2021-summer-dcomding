left, right = list(), list()
for key in input():
    try:
        if key == '<':
            right.append(left.pop())
        elif key == '>':
            left.append(right.pop())
        elif key == '-':
            left.pop()
        else:
            left.append(key)
    except IndexError:
        continue
print(''.join(left+right))

from collections import deque

left, right = deque(), deque() #stack
for key in input():
    try:
        if key == '<':
            right.appendleft(left.pop())
        elif key == '>':
            left.append(right.popleft())
        elif key == '-':
            left.pop()
        else:
            left.append(key)
    except IndexError:
        continue
print(''.join(left+right))

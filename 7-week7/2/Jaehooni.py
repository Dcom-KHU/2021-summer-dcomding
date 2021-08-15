from collections import deque
string = list(input())
left_word = []
right_word = deque()

for i in string:
    if i == "<":
        if left_word:
            right_word.appendleft(left_word.pop())

    elif i == ">":
        if right_word:
            left_word.append(right_word.popleft())

    elif i == "-":
        if left_word:
            left_word.pop()

    else:
        left_word.append(i)

for i in left_word:
    print(i, end = "")

for i in right_word:
    print(i, end = "")


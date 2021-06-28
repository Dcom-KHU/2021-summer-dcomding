from collections import deque

length, turn = map(int, input().split())
inputMap = map(int, input().split())

inputList = sorted(list(inputMap))

deq = deque(inputList)

for i in range(1, turn + 1):
    if (i % 2 == 0):
        deq.pop()

    else:
        deq.popleft()

    length -= 1


sum = 0
for i in range(0, length):
    sum += deq.pop()


print(sum)

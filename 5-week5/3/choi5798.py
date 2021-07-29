import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
timetable = []
using_list = []
count = [0 for _ in range(n)]
index = [i for i in range(n)]
answer = 0
for _ in range(n):
    start, end = map(int, input().split())
    timetable.append([start, end])

timetable.sort(key=lambda x:(x[0], x[1]))
timetable = deque(timetable)
heapq.heapify(index)

time = 0
while timetable:
    if using_list and using_list[0][0] == time:
        end, start, idx = heapq.heappop(using_list)
        heapq.heappush(index, idx)

    if timetable[0][0] == time:
        start, end = timetable.popleft()
        idx = heapq.heappop(index)
        heapq.heappush(using_list, [end, start, idx])
        count[idx] += 1
        continue
    
    time += 1


for i in count:
    if i == 0:
        break
    answer += 1
print(answer)
print(*count[:answer])
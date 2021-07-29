#총 컴퓨터 갯수 answer
#각 컴퓨터당 사용 횟수 count
import sys
import heapq
from collections import deque
input = sys.stdin.readline
n = int(input())
timetable = {}
answer = 0
count = [0 for _ in range(n)]
index = [i for i in range(n)]
using_list = []
for _ in range(n):
    start, end = map(int, input().split())
    if start not in timetable:
        timetable[start] = [end]
    else:
        timetable[start].append(end)

for key in timetable.keys():
    timetable[key] = deque(sorted(timetable[key]))
heapq.heapify(index)

for key in sorted(timetable.keys()):
    while timetable[key]:
        if using_list and using_list[0][0] <= key: # 끝내기
            end, start, idx = heapq.heappop(using_list)
            heapq.heappush(index, idx)
        
         # 시작하기
        start = key
        end = timetable[key].popleft()
        idx = heapq.heappop(index)
        heapq.heappush(using_list, [end, start, idx]) # end 순으로 정렬
        count[idx] += 1

for i in count:
    if i == 0:
        break
    answer += 1

print(answer)
print(*count[:answer])
    


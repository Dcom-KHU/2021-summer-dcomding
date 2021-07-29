#총 컴퓨터 갯수 answer
#각 컴퓨터당 사용 횟수 count
import sys
import heapq
from collections import deque
input = sys.stdin.readline
n = int(input())
timetable = []
answer = 0
count = [0 for _ in range(n)]
index = [i for i in range(n)]
using_list = []
for _ in range(n):
    start, end = map(int, input().split())
    timetable.append([start, end])

timetable.sort(key=lambda x:(x[0], x[1]))
timetable = deque(timetable)
heapq.heapify(index)

time = 0
while timetable:
    
    if using_list and using_list[0][0] == time: # 끝내기
        end, start, idx = heapq.heappop(using_list)
        heapq.heappush(index, idx)
    
    if timetable[0][0] == time: # 시작하기
        start, end = timetable.popleft()
        idx = heapq.heappop(index)
        heapq.heappush(using_list, [end, start, idx]) # end 순으로 정렬
        count[idx] += 1
        continue
    
    time += 1

for i in count:
    if i == 0:
        break
    answer += 1

print(answer)
print(*count[:answer])
    


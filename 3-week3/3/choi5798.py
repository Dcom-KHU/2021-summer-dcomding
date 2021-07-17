# 10 1 5 5
# 9 0
# 9 0
# 9 0
# 9 0
# 9 0
# 답은 9 9
from collections import deque
def minus_1min(hour, minute):
    if minute == 0:
        minute = 59
        hour -= 1
    else:
        minute -= 1
    return [hour, minute]
n, t, m, k = map(int, input().split())
timetable = {}
buses = deque([(9, 0)])
students = 0
answer = []
#bus시간표 만들기
for i in range(n-1):
    hour, minute = buses[-1][0], buses[-1][1]
    if minute + t >= 60:
        minute += t - 60
        hour += 1
    else:
        minute += t
    buses.append((hour, minute))
#학생들 오는 시간표 만들기
for _ in range(k):
    hour, minute = map(int, input().split())
    if timetable.get((hour, minute)) is None:
        timetable[(hour, minute)] = 1
    else:
        timetable[(hour, minute)] += 1

times = deque(sorted(timetable.keys()))
#버스가 오는 시간을 기준으로 먼저 온 사람과 늦게 온 사람을 나눈다
#먼저오거나 시간에 맞춰 온 사람만 세면 되니까 다 세준다
#그 사람들만으로 이미 정원이 넘치는 경우 -> 넘치는 시간에 -1분이 답
#정원이 충분한 경우 -> 버스가 오는 시간이 답

while buses:
    bus = buses.popleft()
    bus_hour, bus_minute = bus[0], bus[1]
    while times:
        time = times.popleft()
        hour, minute = time[0], time[1]
        if hour<bus_hour or (hour==bus_hour and minute<=bus_minute):
            students += timetable[time]
        else:
            times.appendleft(time)
            break
    if students < m:
        answer = list(bus)
        # print('under_answer:', answer)
    else:
        answer = minus_1min(hour, minute)
    students -= m if students - m >= 0 else 0



print(*answer)
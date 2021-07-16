from collections import deque
n, t, m, k = map(int, input().split())
timetable = {}
buses = deque([(9, 0)])
students = 0
answer = []
for i in range(n-1):
    hour, minute = buses[-1][0], buses[-1][1]
    if minute + t >= 60:
        minute += t - 60
        hour += 1
    else:
        minute += t
    buses.append((hour, minute))
for _ in range(k):
    hour, minute = map(int, input().split())
    if timetable.get((hour, minute)) is None:
        timetable[(hour, minute)] = 1
    else:
        timetable[(hour, minute)] += 1

times = deque(sorted(timetable.keys()))
while buses:
    bus = buses.popleft()
    bus_hour, bus_minute = bus[0], bus[1]
    students = 0
    while times:
        key = times.popleft()
        hour, minute = key[0], key[1]
        if hour<bus_hour or (hour==bus_hour and minute <= bus_minute):
            if students + timetable[key] >= m:
                if minute == 0:
                    hour -= 1
                    minute = 59
                else:
                    minute -= 1
                answer = [hour, minute]
                students += timetable[key]
                break
            students += timetable[key]
        else:
            times.appendleft(key)
            answer = list(bus)
            break
    if students < m:
        answer = list(bus)
    if not times:
        break


print(*answer)
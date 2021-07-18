'n: 운행 횟수, t: 운행 간격(분), m: 최대 승객, k: 셔틀 타는 학생 수'
n, t, m, k = map(int, input().split())
timetables = sorted([list(map(int, input().split())) for i in range(k)], key=lambda timetable: (timetable[0], timetable[1]))
stop_times = [[(9 + ((i-1) * t) // 60, ((i-1) * t) % 60)] + [0] for i in range(1, n+1)]
safe_time = []

# print(timetables)
# print(stop_times)

for timetable in timetables:
    for stop_time in stop_times:
        if (stop_time[1] < m):
            if (timetable[0] < stop_time[0][0]):
                stop_time[1] += 1
                safe_time.append(timetable)
                break

            elif (timetable[0] == stop_time[0][0] and timetable[1] <= stop_time[0][1]):
                stop_time[1] += 1
                safe_time.append(timetable)
                break

            else:
                pass

        else:
            pass

if (len(safe_time) == len(timetables)):
    if (stop_times[-1][1] >= m):
        if (safe_time[-1][1] == 0):
            print(safe_time[-1][0] - 1, 59)

        else:
            print(safe_time[-1][0], safe_time[-1][1] - 1)

    else:
        print(stop_times[-1][0][0], stop_times[-1][0][1])
    # print(safe_time[-1][0], safe_time[-1][1] - 1 if stop_times[-1][1] == m else stop_times[-1][0][0], stop_times[-1][0][1])

elif (len(safe_time) == 0):
    print(stop_times[-1][0][0], stop_times[-1][0][1])

else:
    print(safe_time[-1][0], safe_time[-1][1] - 1)

# print(timetables)
# print(stop_times)
# print(safe_time)
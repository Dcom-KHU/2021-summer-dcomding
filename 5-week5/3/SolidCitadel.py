n = int(input())
timetable = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: (x[0], x[1]))

room = [[timetable.pop(0)[1]]]
for time in timetable:
    flag = True
    for seat in room:
        if seat[-1] <= time[0]:
            seat.append(time[1])
            flag = False
            break
    if flag:
        room.append([time[1]])

print(len(room))
for seat in room:
    print(len(seat), end=' ')

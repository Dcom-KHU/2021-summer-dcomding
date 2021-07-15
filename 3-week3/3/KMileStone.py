n, t, m, k = map(int, input().split())
timetable = []
for i in range(k):
    hr, mn = map(int, input().split())
    timetable.append(hr*60+mn)


# sort timetable
timetable.sort()

deadline = 0
first_bus = 9*60+0
passenger = 0
not_full = False

for bus in range(first_bus, first_bus + n*t, t):
    not_full = False

    for i in range(m):
        # if passenger come before bus
        if passenger < k and timetable[passenger] <= bus:
            passenger += 1

        # if passenger late
        else:
            not_full = True
            break

# if not all passenger take bus
if passenger < k:
    # no one can take bus means all passenger late, you can take last bus
    if passenger == 0:
        deadline = first_bus + (n-1)*t

    # not all passenger can take bus means lack of bus, you should queue before last passenger
    else:
        deadline = timetable[passenger-1] - 1

# if all passenger take bus
else:
    # if last bus was not full, you can take last bus
    if not_full:
        deadline = first_bus + (n-1)*t

    # if last bus was full, you should queue before last passenger
    else:
        deadline = timetable[passenger-1] - 1


print(deadline//60, deadline%60)

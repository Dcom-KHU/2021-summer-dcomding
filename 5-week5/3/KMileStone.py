n = int(input())
timetable = []
for i in range(n):
    timetable.append(tuple(map(int, input().split())))


# sort
timetable.sort(key=lambda x: x[0]*1000000 + x[1])

computers = []
found = False

for user in timetable:
    # use existing computer
    for computer in computers:
        if computer[-1][1] <= user[0]:
            computer.append(user)
            found = True
            break

    # use new computer
    if not found:
        computers.append([user])
    else:
        found = False


print(len(computers))
for computer in computers:
    print(len(computer), end=' ')

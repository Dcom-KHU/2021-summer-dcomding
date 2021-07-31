n = int(input())
timetable = []
for i in range(n):
    timetable.append(tuple(map(int, input().split())))


# sort
timetable.sort(key=lambda x: x[0])

computers = []
found = False

for user in timetable:
    # use existing computer
    for computer in computers:
        for j in range(len(computer)):
            # if gap between adjacent user is big enough or after last user
            if computer[j][1] <= user[0]:
                if (j+1 < len(computer) and computer[j+1][0] >= user[1]) or j+1 == len(computer):
                    computer.append(user)
                    found = True
                    break

        if found:
            break

    # use new computer
    if not found:
        computers.append([user])
    else:
        found = False


print(len(computers))
for computer in computers:
    print(len(computer), end=' ')

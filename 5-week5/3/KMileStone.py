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
        if len(computer):
            # binary search
            left = 0
            right = len(computer)-1

            while left <= right:
                mid = (left + right) // 2

                if computer[mid][1] <= user[0]:
                    # if gap between adjacent user is big enough or after last user, found
                    if (mid+1 < len(computer) and computer[mid+1][0] >= user[1]) or mid+1 == len(computer):
                        computer.insert(mid+1, user)
                        found = True
                        break
                    else:
                        left = mid+1
                else:
                    right = mid-1

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

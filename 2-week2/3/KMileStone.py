n = int(input())
tickets = {}
for i in range(n):
    src, dst = input().split()
    tickets.setdefault(src, [])
    tickets[src].append(dst)


# tickets : {src1:[dst1, dst2, ...], src2:[dst1, dst2, ...], ...}
# sort dst lists
for key in tickets:
    tickets[key].sort(key=lambda x : 'a' * len(x) + x)


route = ['DCOM']
prev = 'DCOM'
next = tickets['DCOM'].pop(0)
valid = True

while len(route) < n:
    # if get None or empty list, no further possible route before use all tickets
    if valid:
        valid = bool(tickets.get(next))

    # next possible route
    if valid == True:
        route.append(next)
        prev = next
        next = tickets[next].pop(0)

    # choose another route
    elif valid == False:
        # undo
        tickets[prev].append(next)

        i = 0
        while i < len(tickets[prev])-1 and tickets[prev][i] == tickets[prev][i+1]:
            i += 1

        # if all element of tickets[prev] is same, there is only 1 dst
        # you cannot take another route, more undo
        if i == len(tickets[prev])-1:
            next = route.pop()
            if route:
                prev = route[-1]
            valid = False

        # take another route
        else:
            tickets[prev] = tickets[prev][i:] + tickets[prev][:i]
            new_next = tickets[prev].pop(0)
            prev = next
            next = new_next
            valid = True

# n+1 routes with n tickets
route.append(next)


for club in route:
    print(club, end=' ')

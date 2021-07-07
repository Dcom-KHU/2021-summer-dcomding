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

        # if there is only 1 dst, you cannot take another route
        # more undo
        if len(set(tickets[prev])) == 1:
            next = route.pop()
            if route:
                prev = route[-1]

            # if src == dst, more undo
            while prev == next:
                tickets[prev].append(next)
                next = route.pop()
                if route:
                    prev = route[-1]
            valid = False

        # take another route
        else:
            new_next = tickets[prev].pop(0)
            prev = next
            next = new_next
            valid = True

# n+1 routes with n tickets
route.append(next)


for club in route:
    print(club, end=' ')

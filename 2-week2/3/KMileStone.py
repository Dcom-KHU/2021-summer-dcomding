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
    # no further possible route before use all tickets
    if next not in tickets.keys() or len(tickets[next]) == 0:
        valid = False

    # next possible route
    if valid == True:
        route.append(next)
        prev = next
        next = tickets[next].pop(0)

    # choose another route
    elif valid == False:
        # undo
        tickets[prev].append(next)

        # take another route
        if len(set(tickets[prev])) != 1:
            new_next = tickets[prev].pop(0)
            while new_next == next:
                tickets[prev].append(new_next)
                new_next = tickets[prev].pop(0)
            prev = next
            next = new_next
            valid = True

        # if there is only 1 dst, you cannot take another route
        # more undo
        else:
            next = route.pop()
            if route:
                prev = route[-1]
            valid = False

# n+1 routes with n tickets
route.append(next)


for club in route:
    print(club, end=' ')

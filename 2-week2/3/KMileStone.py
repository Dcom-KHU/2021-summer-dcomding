n = int(input())
tickets = {'self':[]}
for i in range(n):
    src, dst = input().split()
    tickets.setdefault(src, [])
    if src != dst:
        tickets[src].append(dst)
    else:
        tickets['self'].append(dst)


# tickets : {src1:[dst1, dst2, ...], src2:[dst1, dst2, ...], ...}
# sort dst lists
for key in tickets:
    tickets[key].sort(key=lambda x : 'a' * len(x) + x)


route = ['DCOM']
prev = 'DCOM'
next = tickets['DCOM'].pop(0)
valid = True

while len(route) < n-len(tickets['self']):
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

        # take another route
        else:
            new_next = tickets[prev].pop(0)
            prev = next
            next = new_next
            valid = True

# n+1 routes with n tickets
route.append(next)

# add self ticket
def order(x):
    return 'a' * len(x) + x

for self in tickets['self']:
    last = 0
    inserted = False
    for i in range(len(route)):
        if route[i] == self:
            last = i
            if i < len(route)-1 and order(self) < order(route[i+1]):
                route.insert(i, self)
                inserted = True
                break
    if not inserted:
        route.insert(last, self)


for club in route:
    print(club, end=' ')

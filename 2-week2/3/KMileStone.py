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


# DFS
def dfs(prev):
    # add club
    route.append(prev)

    # success : n+1 routes with n tickets
    if len(route) > n:
        return True

    # fail : no further possible route before use all tickets
    elif prev not in tickets.keys() or len(tickets[prev]) == 0:
        return False

    # next possible route
    else:
        for i in range(len(tickets[prev])):
            next = tickets[prev].pop(0)

            # if return is True, break loop and return True in a chain
            if dfs(next):
                return True
            # if return is False, remove club and go on
            else:
                route.pop()

            tickets[prev].append(next)


route = []
dfs('DCOM')

for club in route:
    print(club, end=' ')

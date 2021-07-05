from copy import deepcopy #deepcopy to save previous state of recursion

def nav(n, tickets, now, froute, routes):
    if now in tickets:
        for stop in tickets[now]:
            ticopy = deepcopy(tickets)
            croute = froute + [stop]
            ticopy[now].remove(stop)
            nav(n, ticopy, stop, croute, routes)
            if len(croute) == n + 1:
                routes.append(croute)

n = int(input(""))

#save tickets into dictionary (values in list)
tickets = dict()
for i in range(n):
    k, v = input("").split()
    if k not in tickets.keys():
        tickets[k] = [v]
    else:
        tickets[k].append(v)

#initialise
now = 'DCOM'
route = ['DCOM']
routes = []


nav(n, tickets, now, route, routes)
routes = list(set([tuple(route) for route in routes]))
for x in range(1, n + 2):
    min = 11
    nam = '~'
    for y in range(len(routes)):
        if len(routes[y][x]) < min:
            min = len(routes[y][x])
            nam = routes[y][x]
        elif len(routes[y][x]) == min and routes[y][x] < nam:
            nam = routes[y][x]
    for r in range(len(routes)-1, -1, -1):
        if routes[r][x] != nam:
            routes.remove(routes[r])
    if len(routes) == 1:
        break
route = routes[0]
    

print(' '.join(route))
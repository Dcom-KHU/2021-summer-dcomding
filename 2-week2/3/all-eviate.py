n = int(input(""))

#save tickets into dictionary (values in list)
tickets = dict()
for i in range(n):
    k, v = input("").split()
    if k not in tickets.keys():
        tickets[k] = [v]
    else:
        tickets[k].append(v)

for dept in tickets:
    tickets[dept].sort(key=lambda item: (len(item), item), reverse=True)

#initialise
route = ['DCOM']
path = []

while route:
    now = route[-1]
    if tickets:
        if tickets[now]:
            route.append(tickets[now].pop())
            #if not tickets[now]:
            #    del tickets[now]
        else:
            path.append(route.pop())
    else:
        path.append(route.pop())
path.reverse()
print(' '.join(path))
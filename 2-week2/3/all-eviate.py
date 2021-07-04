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

for i in range(n):
    maxlen = 11
    next = ''
    for stop in tickets[now]: #look for next stop in dictionary of current room
        if len(stop) < maxlen:
            maxlen = len(stop)
            next = stop
    tickets[now].remove(next) #use the ticket (remove from dictionary)
    route.append(next) #save the route
    now = next #move current location

print(' '.join(route))
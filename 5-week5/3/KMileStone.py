import heapq

n = int(input())
timetable = []
for i in range(n):
    timetable.append(tuple(map(int, input().split())))


# sort
timetable.sort(key=lambda x: x[0]*1000000 + x[1])

computer = []

# heap_occupied : [(end time, index of computer), (e, i), (e, i), ...]
# heap_available : [index of computer, i, i, ...]
heap_occupied = []
heap_available = []

for user in timetable:
    # update available
    while heap_occupied and heap_occupied[0][0] <= user[0]:
        heapq.heappush(heap_available, heapq.heappop(heap_occupied)[1])

    # use existing computer
    if heap_available:
        idx = heapq.heappop(heap_available)
        computer[idx] += 1
        heapq.heappush(heap_occupied, (user[1], idx))

    # use new computer
    else:
        computer.append(1)
        heapq.heappush(heap_occupied, (user[1], len(computer)-1))


print(len(computer))
for com in computer:
    print(com, end=' ')

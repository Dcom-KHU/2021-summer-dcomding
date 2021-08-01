import heapq

n = int(input())
timetable = []
for i in range(n):
    timetable.append(tuple(map(int, input().split())))


# sort
timetable.sort(key=lambda x: x[0]*1000000 + x[1])

computer = []

# heap : [(end time, index of computer), (e, i), (e, i), ...]
heap = []

for user in timetable:
    # use existing computer
    if heap and heap[0][0] <= user[0]:
        idx = heapq.heappop(heap)[1]
        computer[idx] += 1
        heapq.heappush(heap, (user[1], idx))

    # use new computer
    else:
        computer.append(1)
        heapq.heappush(heap, (user[1], len(computer)-1))


print(len(computer))
for com in computer:
    print(com, end=' ')

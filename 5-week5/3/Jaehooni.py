n = int(input())
timetable = sorted([tuple(map(int, input().split())) for i in range(n)], key= lambda x: (x[1], x[0]))

l, r = 0, 0
index = 0
#first start time, last end time, user number
seat_list = [[0, 0, 0] for i in range(n)]

for time in timetable:
    if (time[0] < seat_list[index][1]):
        index += 1

    if not (seat_list[index][0]):
        seat_list[index][0] = time[0]
            
    seat_list[index][1] = time[1]
    seat_list[index][2] += 1
    

using_list = sorted(seat_list[:index+1], key= lambda x: x[0])

print(len(using_list))
for i in using_list:
    print(i[2], end=" ")

        
    
            
        
        
    
            
        
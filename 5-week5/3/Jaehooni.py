n = int(input())
timetable = sorted([tuple(map(int, input().split())) for i in range(n)], key= lambda x: (x[1], x[0]))

l, r = 0, 0
#first start time, last end time, user number
seat_list = [[0, 0, 0] for i in range(n)]

'''
l, r로 나타난 2개의 포인터를 가지고
time으로 들어오는 값들의 시작 시간이 l이 가르키고 있는 자리의 end time보다 크다면
l이 가르키고 있는 자리에 집어놓고 l+1
'''
for time in timetable:
    '''
    3 5
    2 6
    5 6
    4 7
    1 8
    6 8
    7 8
    1 11
    '''
    if not seat_list[0][0]:
        seat_list[0][0], seat_list[0][1] = time[0], time[1]
        seat_list[0][2] += 1
        
    elif (time[0] >= seat_list[l][1]):
        seat_list[l][1] = time[1]
        seat_list[l][2] += 1
        seat_list[r+1] = seat_list[l]
        l, r = l+1, r+1
        
    else:
        seat_list[r+1][0], seat_list[r+1][1] = time[0], time[1]
        seat_list[r+1][2] += 1
        r += 1
        

using_list = sorted(seat_list[l:r+1], key= lambda x: x[0])

print(len(using_list))
for i in using_list:
    print(i[2], end=" ")
        
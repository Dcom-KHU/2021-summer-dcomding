n = int(input())
times = [tuple(map(int, input().split())) for i in range(n)]
timetable = dict([(i, True) for i in range(2 << 31)])

def r(times, index, timetable):
    if (index >= len(times)):
        return 0
    
    elif (timestable[times[index][0]+1] or timestable[times[index[index][1]-1]]):
        return r(times, index+1, timetable)
        
    else:
        timetable_copy = timetable_copy()
        for i in range(times[index][0], times[index][1]+1):
            timetable_copy[i] = False
            
        return max(1 + r(times, index+1, timetable_copy), r(times, index+1, timetable))
    
print(r(times,0,timetable))
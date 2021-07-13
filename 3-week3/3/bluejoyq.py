import sys
from collections import deque
input = sys.stdin.readline
def solution():
    num_of_bus,TIME_BETWEEN_BUS,MAX_PASSENGER,NUM_OF_PASSENGER = map(int, input().split())
    timetables = {h:{} for h in range(23)}
    
    for i in range(NUM_OF_PASSENGER):
        # hour, minute
        h,m = map(int, input().split())
        try:
            timetables[h][m] += 1
        except:
            timetables[h][m] = 1
            
    watings = deque([])
    nxt_bus_hour = 9
    nxt_bus_minute = 0
    result = [0,0]
    for hour in range(0,23):
        for minute in range(0,59):
            # 탑승 처리
            try:
                for p in range(timetables[hour][minute]):
                    watings.append([hour,minute])
            except:
                pass
            
            # 
            if nxt_bus_hour == hour and nxt_bus_minute == minute and num_of_bus > 0:
                try:
                    for p in range(MAX_PASSENGER):
                        last = watings.popleft()
                    result = [last[0], last[1] - 1]
                except:
                    result = [hour, minute]
                nxt_bus_minute += TIME_BETWEEN_BUS
                nxt_bus_hour += nxt_bus_minute // 60
                nxt_bus_minute %= 60
                num_of_bus -= 1
                
    print(result)
solution()
            
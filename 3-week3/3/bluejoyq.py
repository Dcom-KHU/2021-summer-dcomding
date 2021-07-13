import sys
from collections import deque
from datetime import timedelta
input = sys.stdin.readline
def solution():
    num_of_bus,TIME_BETWEEN_BUS,MAX_PASSENGER,NUM_OF_PASSENGER = map(int, input().split())
    timetables = {h:{} for h in range(24)}
    
    for i in range(NUM_OF_PASSENGER):
        # hour, minute
        h,m = map(int, input().split())
        try:
            timetables[h][m] += 1
        except:
            timetables[h][m] = 1
    watings = deque([])
    nxt_bus = timedelta(hours = 9, minutes = 0)
    result = timedelta(hours= 0, minutes = 0)
    
    for hour in range(0,23):
        for minute in range(0,60):
            cur = timedelta(hours = hour, minutes = minute)
            
            # 대기열에 사람 추가
            try:
                for p in range(timetables[hour][minute]):
                    watings.append(cur)
            except:
                pass
            
            # 탑승 처리
            
            if nxt_bus == cur and num_of_bus > 0:
                try:
                    for p in range(MAX_PASSENGER):
                        last = watings.popleft()
                    result = last - timedelta(minutes = 1)
                except:
                    result = cur
                nxt_bus += timedelta(minutes = TIME_BETWEEN_BUS)
                num_of_bus -= 1
                
    print(result.seconds // 3600, (result.seconds//60)%60)
solution()
            
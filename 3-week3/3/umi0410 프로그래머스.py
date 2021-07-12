# 별 다른 풀이 기법이 있다기보다는 그냥 구현인듯하다.
# timetable을 sort한 뒤 가장 뒤의 셔틀에 태운다.
# 셔틀은 09:00부터 총 n회 t분 간격으로 최대 m명을 태운다.
from collections import defaultdict

def solution(n, t, m, timetable):
    timetable.sort()
    shuttles = defaultdict(list)
    shuttle_times = ['09:00']
    for i in range(n-1):
        new_minute = (t * (i + 1)) % 60
        new_hour = 9 + (t * (i + 1)) // 60
        shuttle_times.append('{0:02d}:{1:02d}'.format(new_hour, new_minute))
    for crew in timetable:
        # print(crew)
        for shuttle_time in shuttle_times:
            if crew <= shuttle_time and len(shuttles[shuttle_time]) < m:
                shuttles[shuttle_time].append(crew)
                break
    # print(shuttles)
    # print(shuttle_times)
    if len(shuttles[shuttle_times[-1]]) == m:
        last_crew = shuttles[shuttle_times[-1]][-1]
        # 내림 연산 필요
        return '{0:02d}:{1:02d}'.format((get_minute(last_crew) - 1) // 60 + get_hour(last_crew), (60 + get_minute(last_crew) - 1) % 60)

    return shuttle_times[-1]


def get_hour(text):
    return int(text[:2])

def get_minute(text:str):
    return int(text[3:5])

print(solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,	2,	["09:10", "09:09", "08:00"]))
print(solution(2,	1,	2,	["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,	1,	5,	["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1,	1,	1,	["23:59"]))
print(solution(10,	60,	45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

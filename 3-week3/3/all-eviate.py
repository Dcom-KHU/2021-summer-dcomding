'''
n = number of cars
t = term of cars (minutes)
m = maximum capacity per cars
k = students waiting in queue
'''
import operator


class time: # definition of time class for operator overloading
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __lt__(self, other):
        if self.h != other.h:
            return self.h < other.h
        else:
            return self.m < other.m
    def __le__(self, other):
        if self.h < other.h:
            return True
        elif self.h == other.h:
            return self.m <= other.m
        else:
            return False
    def __eq__(self, other):
        return self.h == other.h and self.m == other.m
    def __add__(self, num):
        if isinstance(num, int):
            return time(self.h + (self.m + num)//60, (self.m + num)%60)
    def __sub__(self, num):
        if isinstance(num, int):
            if self.m >= num:
                return time(self.h, self.m - num)
            else:
                return time(self.h - 1, 60 + self.m - num)
        if isinstance(num, time):
            if self.m >= num.m:
                return time(self.h - num.h, self.m - num.m)
            else:
                return time(self.h - 1 - num.h, self.m - num.m + 60)


n, t, m, k = map(int, input().split())
max_cap = m * n
carsch = []
for c in range(n):
    carsch.append(time(9, 0) + c * t)
last_car_full = False
tt = []
competitors_count = 0
for i in range(k):
    hour, minute = map(int, input().split())
    tt.append(time(hour, minute))
    
tt = sorted(tt, key = operator.attrgetter('h', 'm'))

stuind = 0

for c in range(n):
    if stuind >= max_cap:
        break
    seats_taken = 0
    for s in range(stuind, k):
        if tt[s] <= carsch[c]:
            linq = tt[s]
            stuind += 1
            seats_taken += 1
        else:
            break
        if seats_taken >= m:
            if c == n-1:
                last_car_full = True
            break

if not last_car_full and stuind <= max_cap: # all students aboard still seats left
    print(f'{carsch[-1].h} {carsch[-1].m}')
else:
    print(f'{(linq-1).h} {(linq-1).m}')

# print(f'm = {m}')
# print(f'stuind = {stuind}')
# print(f'last time = {linq.h} {linq.m}')

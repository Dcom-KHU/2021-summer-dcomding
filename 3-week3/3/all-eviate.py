'''
n = number of cars
t = term of cars (minutes)
m = maximum capacity
k = students waiting in queue
'''
import operator

class time: # definition of time class for operator overloading
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __lt__(self, other):
        if self.h != other.n:
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
    def __sub__(self, num):
        if isinstance(num, int):
            if self.m >= num:
                return time(self.h, self.m - num)
            else:
                return time(self.h - 1, 60 + self.m - num)
        if isinstance(num, time):
            if self.m >= num:
                return time(self.h - num.h, self.m - num.m)
            else:
                return time(self.h - 1 - num.h, self.m - num.m + 60)


n, t, m, k = map(int, input().split())
last_h = (n - 1) * t // 60 + 9
last_m = (n - 1) * t % 60
last_ride = time(last_h, last_m)
car_full = False
tt = []
competitors_count = 0
for i in range(k):
    hour, minute = map(int, input().split())
    tt.append(time(hour, minute))
    
tt = sorted(tt, key = operator.attrgetter('h', 'm'))

for j in range(k):
    if tt[j] <= last_ride:
        competitors_count += 1
        if not car_full and competitors_count > m:
            target_time = tt[j] - 1
            car_full = True
            break

if m > k: # abundant capacity
    print(f'{last_h} {last_m}')
elif competitors_count < m: # enough seats left
    print(f'{last_h} {last_m}')
elif car_full:
    print(f'{target_time.h} {target_time.m}')
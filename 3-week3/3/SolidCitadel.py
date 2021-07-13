n, t, m, k = map(int, input().split())
passengers = sorted([(lambda x: int(x[0])*60 + int(x[1]))(input().split()) for i in range(k)], reverse=True)

for time in range(9*60 + 0, 23*60 + 59, t)[:n]:
    bus = [passengers.pop() for i in range(m) if passengers and passengers[-1] <= time]
    
if len(bus) == m:
    time = bus[-1] - 1

print(time//60, time%60)

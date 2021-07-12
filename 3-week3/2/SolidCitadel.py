maxi = 0
def fn(schedule, day):
    for i, (t, p) in enumerate(TP[day-1:]):
        i += day-1
        if sum(schedule[i:i+t]) == 0 and i+t <= n:
            ns = schedule[:]
            ns[i:i+t] = [i+1]*t
            fn(ns, i+t+1)
    global maxi
    maxi = max(sum([TP[i-1][1] for i in set(schedule) if i]), maxi)

n = int(input())
TP = [tuple(map(int, input().split())) for i in range(n)]

fn([0]*(n+1), 1)
print(maxi)

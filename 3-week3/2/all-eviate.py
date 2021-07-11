n = int(input(""))
r = []
maxwage = 0

for i in range(n):
    t, p = map(int, input("").split())
    r.append([t, p])

for start in range(n):
    date = start
    wage = 0
    while date < n:
        if r[date][0] <= n-date:
            wage += r[date][1]
        date += r[date][0]
    if wage > maxwage:
        maxwage = wage

print(maxwage)
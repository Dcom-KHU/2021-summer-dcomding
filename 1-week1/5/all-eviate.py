n = int(input(""))
money = list(map(int, input("").split()))
t1 = 0
t2 = 0
mt = money[:]
while max(mt) > 0:
    m = max(mt)
    t1 += m
    ind = mt.index(m)
    for i in range(ind-1, ind+2):
        if i >= 0 and i < n:
            mt[i] = 0
        else:
            mt[(i+n)%n] = 0
mt = money[:]
mt[mt.index(max(mt))] = 0
while max(mt) > 0:
    m = max(mt)
    t2 += m
    ind = mt.index(m)
    for i in range(ind-1, ind+2):
        if i >= 0 and i < n:
            mt[i] = 0
        else:
            mt[(i+n)%n] = 0
if t1 >= t2:
    print(t1)
else:
    print(t2)
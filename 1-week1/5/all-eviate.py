n = int(input(""))
money = list(map(int, input("").split()))
t1 = 0
t2 = 0
mt1 = money[:]
mt2 = money[:]
mt2[mt2.index(max(mt2))] = 0
while max(mt1) > 0:
    m1 = max(mt1)
    t1 += m1
    ind = mt1.index(m1)
    for i in range(ind-1, ind+2):
        if i >= 0 and i < n:
            mt1[i] = 0
        else:
            mt1[(i+n)%n] = 0
    m2 = max(mt2)
    t2 += m2
    ind = mt2.index(m2)
    for i in range(ind-1, ind+2):
        if i >= 0 and i < n:
            mt2[i] = 0
        else:
            mt2[(i+n)%n] = 0
#while max(mt2) > 0:
if t1 >= t2:
    print(t1)
else:
    print(t2)
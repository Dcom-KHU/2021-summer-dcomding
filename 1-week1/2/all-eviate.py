n = int(input(""))
total = 0
for i in range(n):
    m = pow(2, i) #moves count
    if i%2 == 0: #홀수 원판
        s = 3 #start
        for c in range(m):
            total += s
            s -= 1
            if s == 0:
                s = 3
    else: #짝수 원판
        s = 2
        for c in range(m):
            total += s
            s += 1
            if s == 4:
                s = 1

print(total)
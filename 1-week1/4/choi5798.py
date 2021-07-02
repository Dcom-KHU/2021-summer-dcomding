n, k = list(map(int, input().split()))
stones = list(map(int, input().split()))
dcom = 0
now = -1
jump = 1
while True:
    if now + jump < n:
        if stones[now+jump] > 0:
            now += jump
            stones[now] -= 1
            jump = 1
        elif jump < k:
            jump += 1
        else:
            break
    else:
        dcom += 1
        now = -1
        jump = 1
print(dcom)
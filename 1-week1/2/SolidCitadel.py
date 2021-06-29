def hanoi(f, t, n):
    return t if n==1 else hanoi(f, 6-f-t, n-1) + t + hanoi(6-f-t, t, n-1)

print(hanoi(1, 3, int(input())))

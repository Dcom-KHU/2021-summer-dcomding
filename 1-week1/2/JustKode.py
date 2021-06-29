sum_var = 0

def move(N, start, to):
    global sum_var
    sum_var += to

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

n = int(input())
hanoi(n, 1, 3, 2)
print(sum_var)

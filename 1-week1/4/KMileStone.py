n, k = map(int, input().split())
stones = list(map(int, input().split()))


count_zero = 0
max_zero = 0
member = 0

while True:
    for i in range(n):
        if stones[i] == 0:
            count_zero += 1
        else:
            if count_zero > max_zero:
                max_zero = count_zero
            count_zero = 0
            stones[i] -= 1

    # if k zeros in a row, you should jump k+1
    if max_zero >= k:
        break

    # success member
    member += 1

print(member)

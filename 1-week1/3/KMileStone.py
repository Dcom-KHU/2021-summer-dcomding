n = int(input())
seq = list(map(int, input().split()))
n_add, n_sub, n_mul, n_div = map(int, input().split())


max_val = float("-inf")
min_val = float("inf")

# recursive
def calc(prev, i, n_add, n_sub, n_mul, n_div):
    global max_val
    global min_val

    if i == n:
        if prev > max_val:
            max_val = prev
        if prev < min_val:
            min_val = prev
        return

    elif i < n:
        # add
        if n_add > 0:
            calc(prev + seq[i], i + 1, n_add - 1, n_sub, n_mul, n_div)

        # sub
        if n_sub > 0:
            calc(prev - seq[i], i + 1, n_add, n_sub - 1, n_mul, n_div)

        # mul
        if n_mul > 0:
            calc(prev * seq[i], i + 1, n_add, n_sub, n_mul - 1, n_div)

        # div
        if n_div > 0:
            calc(int(prev / seq[i]), i + 1, n_add, n_sub, n_mul, n_div - 1)


calc(seq[0], 1, n_add, n_sub, n_mul, n_div)
print(max_val)
print(min_val)

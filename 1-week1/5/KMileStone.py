n = int(input())
money = list(map(int, input().split()))


# n = 3 : [1 2 3]           -> 1 2 3 1 2 3                  -> [1] [2] [3]
# n = 4 : [1 2 3 4]         -> 1 2 3 4 1 2 3 4              -> [1 3] [2 4]
# n = 5 : [1 2 3 4 5]       -> 1 2 3 4 5 1 2 3 4 5          -> [1 3] [2 4] [3 5] [4 1] [5 2]
# n = 6 : [1 2 3 4 5 6]     -> 1 2 3 4 5 6 1 2 3 4 5 6      -> [1 3 5] [2 4 6]
# n = 7 : [1 2 3 4 5 6 7]   -> 1 2 3 4 5 6 7 1 2 3 4 5 6 7  -> [1 3 5] [2 4 6] [3 5 7] [4 6 1] [5 7 2] [6 1 3] [7 2 4]
# ...

# circulate money
money_circ = money + money

val = 0
max_val = 0

for i in range(n):
    val = 0

    # you can steal maximum n//2 laptops in non-neighbor
    for j in range(n//2):
        val += money_circ[i + 2*j]

    # update max
    if val > max_val:
        max_val = val

print(max_val)

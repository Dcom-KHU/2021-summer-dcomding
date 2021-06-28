n = int(input())


# n = 1 : 3                                     -> 1st plate 1 to 3
# n = 2 : 2 / 3 / 3                             -> 1-layer tower 1 to 2 / 2nd plate 1 to 3 / 1-layer tower 2 to 3
# n = 3 : 3 2 2 / 3 / 1 3 3                     -> 2-layer tower 1 to 2 / 3rd plate 1 to 3 / 2-layer tower 2 to 3
# n = 4 : 2 3 3 2 1 2 2 / 3 / 3 1 1 3 2 3 3     -> 3-layer tower 1 to 2 / 4th plate 1 to 3 / 3-layer tower 2 to 3
# n = 5 : [n=4 swap 2,3] / 3 / [n=4 swap 1,2]   -> 4-layer tower 1 to 2 / 5th plate 1 to 3 / 4-layer tower 2 to 3
# ...

prev_step = []
result = []

for iter in range(n):
    # reset result
    result = []

    # prev_step swap 2,3
    for e in prev_step:
        if e == 2:
            result.append(3)
        elif e == 3:
            result.append(2)
        else:
            result.append(e)

    # iter-th plate
    result.append(3)

    # prev_step swap 1,2
    for e in prev_step:
        if e == 1:
            result.append(2)
        elif e == 2:
            result.append(1)
        else:
            result.append(e)

    # update prev_step
    prev_step = result.copy()

# sum total step
print(sum(result))

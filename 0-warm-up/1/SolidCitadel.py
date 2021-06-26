n = int(input())

if 1 <= n and n <= 9:
    for i in range(min(n, 3)):
        print(f"{n} * {i+1} = {n*(i+1)}")

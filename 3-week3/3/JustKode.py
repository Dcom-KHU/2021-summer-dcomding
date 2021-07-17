n, t, m, k = map(int, input().split())
nine_o_clock = 9 * 60
last_bus = nine_o_clock + t * (n - 1)
list_var = []

def func(l):
    return int(l[0]) * 60 + int(l[1])

def func2(x):
    return str(x // 60) + ' ' + str(x % 60)

for _ in range(k):
    list_var.append(func(input().split()))

list_var.sort()

index = 0
answer = 0

for bus in range(n):
    time = nine_o_clock + bus * t
    in_bus = 0
    
    while in_bus < m and index < k and list_var[index] <= time:
        index += 1
        in_bus += 1
    
    if in_bus < m:
        answer = time
    else:
        answer = list_var[index - 1] - 1

print(func2(answer))


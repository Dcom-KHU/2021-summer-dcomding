n = int(input())
a = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_var = 1000000001
max_var = -1000000001

def operating(current, depth):
    global min_var, max_var, plus, minus, multiply, divide, string

    if depth == n - 1:
        min_var = min(current, min_var)
        max_var = max(current, max_var)
        return
    
    if depth == 0:
        if plus > 0:
            plus -= 1
            operating(a[depth] + a[depth + 1], depth + 1)
            plus += 1
        if minus > 0:
            minus -= 1
            operating(a[depth] - a[depth + 1], depth + 1)
            minus += 1
        if multiply > 0:
            multiply -= 1
            operating(a[depth] * a[depth + 1], depth + 1)
            multiply += 1
        if divide > 0:
            divide -= 1
            if (a[depth] > 0 and a[depth + 1] > 0) or (a[depth] > 0 and a[depth + 1] > 0):
                operating(a[depth] // a[depth + 1], depth + 1)
            else:
                operating(-(abs(a[depth]) // abs(a[depth + 1])), depth + 1)
            divide += 1
    else:
        if plus > 0:
            plus -= 1
            operating(current + a[depth + 1], depth + 1)
            plus += 1
        if minus > 0:
            minus -= 1
            operating(current - a[depth + 1], depth + 1)
            minus += 1
        if multiply > 0:
            multiply -= 1
            operating(current * a[depth + 1], depth + 1)
            multiply += 1
        if divide > 0:
            divide -= 1
            if (current > 0 and a[depth + 1] > 0) or (current > 0 and a[depth + 1] > 0):
                operating(current // a[depth + 1], depth + 1)
            else:
                operating(-(abs(current) // abs(a[depth + 1])), depth + 1)
            divide += 1

operating(0, 0)

print(max_var)
print(min_var)
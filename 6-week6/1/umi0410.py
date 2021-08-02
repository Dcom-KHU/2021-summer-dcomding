N = int(input())
t = 1
while t < N:
    t *= 2

if N < t:
    t //= 2
print(t)
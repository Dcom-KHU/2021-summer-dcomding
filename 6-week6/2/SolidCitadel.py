a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count, i = 0, 0
for an in A:
    while i < b and B[i] <= an:
        if B[i] == an:
            count += 1
        i += 1
        
print(a + b - 2*count)

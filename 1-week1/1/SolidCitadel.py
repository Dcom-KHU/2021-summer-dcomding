n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for i in range(1, k+1):
    if i%2:
        arr.remove(min(arr))
    else:
        arr.remove(max(arr))

print(sum(arr))

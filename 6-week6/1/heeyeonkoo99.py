n = int(input())
arr = [i+1 for i in range(n)]
tmp = []
while len(arr) != 1:
    for idx, item in enumerate(arr):
        if idx % 2:
            tmp.append(item)
    arr = tmp
    tmp = []
print(arr[0])
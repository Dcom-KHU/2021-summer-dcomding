n, m = map(int, input().split())
blocks = list(map(int, input().split()))


sum = 0
count = 0
center = 0
base = 0

# check from last block
while blocks and base-m < center < base+m:
    sum += blocks.pop()
    count += 1
    center = sum / count
    try:
        base = blocks[-1]
    except:
        break


if count == n:
    print(1)
else:
    print(0)

n, m = map(int, input().split())
blocks = list(map(int, input().split()))


sum = 0
count = 0
center = 0
base = 0

# check from last block
while blocks and base-m < center < base+m:
    sum += base
    count += 1
    center = sum / count
    base = blocks.pop()


if count == n:
    print(1)
else:
    print(0)

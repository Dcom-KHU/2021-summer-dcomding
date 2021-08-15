n = int(input())
cookies = list(map(int, input().split()))

maxi = 0
for i in range(n-1):
    left, right = i, i+1
    leftsum, rightsum = cookies[left], cookies[right]
    while True:
        if maxi < leftsum == rightsum:
            maxi = rightsum
        elif 0 < left and leftsum <= rightsum:
            left -= 1
            leftsum += cookies[left]
        elif right < n-1 and leftsum >= rightsum:
            right += 1
            rightsum += cookies[right]
        else:
            break
print(maxi)

def solve():
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    MAX = 10001
    nums = [0] * MAX
    for value in values: # N 한번
        nums[value] += 1
    
    back = K//2
    front = K - back
    i = -1
    while front > 0:
        i += 1
        front -= nums[i]
        nums[i] = 0
    try:
        # front가 마이너스일 경우 마지막 숫자 그만큼 복구
        nums[i] -= front 
    except:
        pass
    
    i = MAX
    while back > 0:
        i -= 1
        back -= nums[i]
        nums[i] = 0
    try:
        # back이 마이너스일 경우 마지막 숫자 그만큼 복구
        nums[i] -= back 
    except:
        pass
    
    for i in range(MAX):
        nums[i] = nums[i] * i
    result = sum(nums)
    
    print(result)
solve()
import math
def solve():
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    MAX = 10001
    nums = [0] * MAX
    for value in values: # N 한번
        nums[value] += 1
    
    front = math.ceil(K / 2)
    back = K//2
    #print(front, back)
    i = -1
    while front > 0:
        i += 1
        front -= nums[i]
        nums[i] = 0
    try:
        nums[i] -= front # front가 마이너스일 경우 
    except:
        pass
    i = MAX
    while back > 0:
        i -= 1
        back -= nums[i]
        nums[i] = 0
    try:
        nums[i] -= back # back이 마이너스일 경우 
    except:
        pass
    result = sum([nums[i] * i for i in range(MAX)])
    
    print(result)
solve()
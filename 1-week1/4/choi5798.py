n, k = list(map(int, input().split()))
stones = list(map(int, input().split()))
MIN = 1
MAX = max(stones)
answer = 0
def check(stones, k, mid):
    cnt=0
    for i in range(len(stones)):
        if stones[i] < mid:
            cnt+=1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

while MIN <= MAX:
    mid = (MIN + MAX) // 2
    if check(stones, k, mid):
        MIN = mid + 1
        if answer < mid:
            answer = mid
    else:
        MAX = mid - 1
print(answer)
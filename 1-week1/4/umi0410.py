# 징검다리를 순수하게 계속 aging 시켜야할까?
# 우선은 aging 시키는 방향으로 해봄
# => 효율성에서 시간 때문에 다 틀렸음.
# => 매번 aging 시킬 필요 없이 지나간 사람 수를 통해 비교할 수 있음
# => 게다가 그 적당한 사람 수를 한 쪽 끝에서부터 1씩 증가/감소 하면서 찾지 말고
#    이진탐색을 통해 찾을 것.
def solution(stones, k):
    left = min(stones)
    right = max(stones)
    # 이진탐색은 left와 right가 대소관계가 유지될 때 까지 진행됨.

    while left <= right:
        mid = (left + right) // 2
        is_verified = verify(stones, mid, k)
        # 더 많은 친구를 넘겨봐
        if is_verified:
            left = mid + 1
        else:
            right = mid - 1
    # left가 더 커져버린 경우 right이 우리가 찾는 값이다.
    # 언제가 우리가 찾는 값이 나오는지 판단하는 게 중요!
    return right

# friend는 몇 번째 friend인지
# 3번 째 friend는 3보다 크거나 같은 stone을 밟을 수 있다.
def verify(stones, friend, k):
    width = 0
    for stone in stones:
        if stone < friend:
            width += 1
            if width >= k: return False
        else:
            width = 0
    return True

# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
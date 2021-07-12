# 조합 후 set 한 뒤 각
def solution(nums, MAX):
    numOfKinds = len(set(nums))
    return int(min(MAX, numOfKinds))
_, MAX = map(int, input().split())
print(solution(map(int, input().split()), MAX))
# print(solution([3,1,2,3]))
# print(solution([3,3,3,2,2,4]))
# print(solution([3,3,3,2,2,2]))
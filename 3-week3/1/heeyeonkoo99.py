#3주차-1
n,k=map(int,input().split())
nums=list(map(int,input().split()))
def solution(nums):
    answer=0
    temp=list(set(nums))

    for value in temp:
        if answer<k:
            answer+=1
    return answer
print(solution(nums))
#항상 어떻게 하면 더 단순하고 직관적으로 구현할수 있을지 생각하자.
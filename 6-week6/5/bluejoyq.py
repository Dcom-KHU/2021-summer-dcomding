from collections import deque
def solution():
    n,k = map(int, input().split())
    values = list(map(int, input().split()))
    
    if k >= sum(values):
        return -1
    
    # value 순으로 정렬한다.
    sorted_values = deque(sorted([(values[idx],idx) for idx in range(len(values))]))
    
    # (min_value의 증가치 * 남은 sorted_values의 길이)를 k보다 클때까지. 계속 빼준다.
    lst_min_val = 0
    while sorted_values:
        min_val, min_idx = sorted_values[0]
        cur_minus = (min_val - lst_min_val) * len(sorted_values)
        if k > cur_minus:
            k -= cur_minus
            sorted_values.popleft()
        else:
            break
    
    # 더이상 sorted_values의 길이가 줄어들 일은 없다.
    rest_value_len = len(sorted_values)
    k %= rest_value_len
    
    # 다시 idx순으로 정렬. val은 중요하지 않음 이제.
    rest_values = sorted([idx for val, idx in sorted_values])
    return(rest_values[k])


print(solution())
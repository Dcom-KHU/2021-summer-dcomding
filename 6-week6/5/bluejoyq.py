from collections import deque
def solution():
    n ,k =map(int, input().split())
    values = list(map(int, input().split()))
    if k >= sum(values):
        return -1
    idx_by_val = {}    
    for idx in range(n):
        try:
            idx_by_val[values[idx]].append(idx)
        except:
            idx_by_val[values[idx]] = [idx]
    # key를 value 순으로 정렬한다.
    sorted_key_idx_by_val = deque(sorted(idx_by_val.keys()))
    
    # (min_value의 증가치 * 남은 values의 길이)를 k보다 클때까지. 계속 빼준다.
    lst_min_val = 0
    while sorted_key_idx_by_val:
        
        min_val = sorted_key_idx_by_val[0]
        cur_minus = (min_val - lst_min_val) * n
        if k >= cur_minus:
            k -= cur_minus
            delete_key = sorted_key_idx_by_val.popleft()
            n -= len(idx_by_val[delete_key])
            del idx_by_val[delete_key]
            lst_min_val = min_val
        else:
            break
    
    # 더이상 남은 value의 길이가 줄어들 일은 없다.
    k %= n
    # 다시 idx순으로 정렬. val은 중요하지 않음 이제.
    rest_values = []
    for tmp in idx_by_val.values():
        rest_values.extend(tmp)
    rest_values.sort()
    return(rest_values[k])
print(solution())

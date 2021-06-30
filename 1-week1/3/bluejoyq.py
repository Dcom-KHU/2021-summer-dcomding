import sys
import math

def solve():
    MAX = sys.maxsize
    N = int(input())
    values = list(map(int, input().split()))
    cals = list(map(int, input().split()))
    max_result = -MAX
    min_result = MAX

    cur = values[0]

    def find_max_min(N,values,cals, max_result, min_result, now, cur):
        if now == N:
            max_result = max(max_result, cur)
            min_result = min(min_result, cur)
            return ;
        now_val = values[now]
        for cal_idx in range(4):
            if not cals[cal_idx]:
                continue
            cals[cal_idx] -= 1
            nxt = cur


            if cal_idx == 0:
                nxt = cur + now_val
            elif cal_idx == 1:
                nxt = cur - now_val
            elif cal_idx == 2:
                nxt = cur * now_val
            else:
                if cur < 0:
                    nxt = - math.floor(abs(cur) / now_val)
                else:
                    nxt = math.floor(cur / now_val)
            find_max_min(N,values,cals, max_result, min_result,now + 1 , nxt)
            cals[cal_idx] += 1
    find_max_min(N,values,cals, max_result, min_result,1, cur)
    print(max_result)
    print(min_result)
# 컴퓨터는 최대 10만대가 필요할 수도 있는데
# 이걸 어느 세월에 하나 하나 확인할까? 이진탐색을 써야할 듯
import sys
input = sys.stdin.readline
from heapq import *

N = int(input())
table = []
for _ in range(N):
    start, finish = map(int, input().split())
    # 일찍 시작할 수록 우선순위가 높고, 빨리 끝날 수록 우선순위가 높음
    table.append((start, finish))
table.sort()
# index와 finish time
# 사용 중인 컴퓨터. (finish_time, idx)
# 사용중인 컴퓨터를 끝내기 위한 정렬에는 finish_time이 중요하고 idx는 실제 끝낼 정보를 담음
using_computers = []
# 놀고있는 컴퓨터. 놀고 있는 컴퓨터 중 사용할 컴퓨터를 찾기 위해선 idx가 중요함.
idle_computers = [0]
# 각 컴퓨터의 사용자 수를 기록
user_numbers = [0]
for start, finish in table:
    # 가장 일찍 사용이 끝난 computer을 사용할 것임
    # 끝낼 컴퓨터를 선형적으로 앞에서부터 찾는 것은 O(N)
    # heap은 O(log N)
    while using_computers:
        _finish, computer = heappop(using_computers)
        # 끝낼 컴퓨터가 없는 거임
        if start < _finish:
            heappush(using_computers, [_finish, computer])
            break
        else:
            heappush(idle_computers, computer)
    # 어떤 컴퓨터를 사용할 지 노는 컴퓨터 중 앞에서부터 찾는 선형적인 방식은
    # O(N)
    # 하지만 heappop은 O(logN)
    if idle_computers:
        computer = heappop(idle_computers)
        user_numbers[computer] += 1
        heappush(using_computers, [finish, computer])
    else:
        user_numbers.append(1)
        heappush(using_computers, [finish, len(user_numbers) - 1])


print(len(user_numbers))
print(' '.join(map(str, user_numbers)))
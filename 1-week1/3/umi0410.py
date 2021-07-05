# # 연산자
# # 연산자들을 permutation 한 뒤 set을 하는 방식으로
# # 중복 개수가 다를 수 있는 중복 순열을 만들었는데
# # 더 좋은 방법은 없을지?
#
# # 설마 브루트포스일까 다른 로직이 있진 않을까 싶은데
# # 그냥 브루트포스인 것 같다..
# from itertools import permutations
# length = int(input())
# nums = list(map(int, input().split()))
# num_of_operators = list(map(int, input().split()))
# # 0: +
# # 1: -
# # 2: *
# # 3: //
# operators = []
# for i, num in enumerate(num_of_operators):
#     operators += [i] * num
#
# operator_perms = set(permutations(operators))
#
# results =[]
# for operators in operator_perms:
#     r = nums[0]
#     for i, operator in enumerate(operators):
#         value = nums[i + 1]
#         if operator == 0:
#             r += value
#         elif operator == 1:
#             r -= value
#         elif operator == 2:
#             r *= value
#         elif operator == 3:
#             if r * value < 0:
#                 r = abs(r)
#                 value = abs(value)
#                 r //= value
#                 r = - r
#             else:
#                 r //= value
#     results.append(r)
#
# # print(results)
# print(max(results))
# print(min(results))
#
#
#

import itertools

def cal(h, o):
    res = nums[0]
    for i in range(0,len(o)):
        if o[i] == '0':
            res += nums[i+1]
        elif o[i] == '1':
            res -= nums[i+1]
        elif o[i] == '2':
            res *= nums[i+1]
        elif o[i] == '3':
            if res < 0:
                res = -((-res)//nums[i+1])
            else:
                res = res//nums[i+1]
    h.append(res)

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
perm = []
for i in range(0, 4):
    for j in range(0, ops[i]):
        perm.append(str(i))
perm = list(map(''.join, itertools.permutations(perm, len(perm))))
history = []
perm_set = set(perm)
perm = list(perm_set)
for i in range(len(perm)):
    cal(history, perm[i])

print(max(history))
print(min(history))
# 연산자
# 연산자들을 permutation 한 뒤 set을 하는 방식으로
# 중복 개수가 다를 수 있는 중복 순열을 만들었는데
# 더 좋은 방법은 없을지?

# 설마 브루트포스일까 다른 로직이 있진 않을까 싶은데
# 그냥 브루트포스인 것 같다..
from itertools import permutations
length = int(input())
nums = list(map(int, input().split()))
num_of_operators = list(map(int, input().split()))
# 0: +
# 1: -
# 2: *
# 3: //
operators = []
for i, num in enumerate(num_of_operators):
    operators += [i] * num

operator_perms = permutations(operators)

results =[]
for operators in operator_perms:
    r = nums[0]
    for i, operator in enumerate(operators):
        value = nums[i + 1]
        if operator == 0:
            r += value
        elif operator == 1:
            r -= value
        elif operator == 2:
            r *= value
        elif operator == 3:
            if r * value < 0:
                r = abs(r)
                value = abs(value)
                r //= value
                r = - r
            else:
                r //= value
    results.append(r)

# print(results)
print(max(results))
print(min(results))




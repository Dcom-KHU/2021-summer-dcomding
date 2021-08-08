a, b = map(int, input().split())
a_list = input().split()
b_list = input().split()
sum_list = a_list + b_list
sum_set = list(set(sum_list))
'합집합'

n = len(sum_list) - len(sum_set)
'두 집합의 원소 개수의 합 - 합집합의 원소 개수 == 교집합의 원소 개수'

print(len(sum_set) - n)
'합집합의 원소 개수 - 교집합의 원소 개수 == 대칭 차집합의 원소 개수'
n = int(input())
value = 1

'''
==> 해당 n보다 작은 수 중에서 가장 큰 2의 제곱수가 답임
'''

while value <= n:
    value *= 2

print(int(value) if value == n else int(value / 2))
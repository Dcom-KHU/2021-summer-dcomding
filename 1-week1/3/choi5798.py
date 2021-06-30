from itertools import permutations
import numpy as np
def calculate(a, b, ch):
    if ch == '+':
        return a+b
    elif ch == '-':
        return a-b
    elif ch == '*':
        return a*b
    elif ch == '/':
        return int(a/b)

n = int(input())
nums = list(map(int, input().split()))
symbol_counts = list(map(int, input().split()))

SYM = ['+', '-', '*', '/']
MAX = -9999
MIN = 9999
symbols = []
for count, sym in zip(symbol_counts, SYM):
    for j in range(count):
        symbols.append(sym)
        
for syms in permutations(symbols, n-1):
    temp = np.int64(calculate(nums[0], nums[1], syms[0]))
    for i in range(2, n):
        temp = np.int64(calculate(temp, nums[i], syms[i-1]))
    if temp > MAX:
        MAX = temp
        # print('MAX:', syms)
    elif temp < MIN:
        MIN = temp
        # print('MIN:', syms)
print(MAX)
print(MIN)
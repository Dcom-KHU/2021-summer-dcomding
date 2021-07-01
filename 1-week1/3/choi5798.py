#-*-coding:utf-8-*-
from collections import Counter
def calculate(a, b, ch):
    if ch == '+':
        return a+b
    elif ch == '-':
        return a-b
    elif ch == '*':
        return a*b
    elif ch == '/':
        return int(a/b)

def helper(prefix, ws):
    #prefix: 이전까지 선택된 순열
    #ws: dict
    #모든 요소를 소진했을 때 prefix를 리턴
    if all(v == 0 for v in ws.values()):
        yield prefix
    #1개 이상 남은 요소가 있으면 prefix에 추가한다
    #해당 요소의 개수를 1차감한 값으로 helper를 다시 호출한다
    for w in ws:
        if ws[w] > 0:
            yield from helper((*prefix, w), {**ws, w:ws[w]-1})
def perms(symbols):
    yield from helper((), Counter(symbols))

n = int(input())
nums = list(map(int, input().split()))
symbol_counts = list(map(int, input().split()))
check = []

SYM = ['+', '-', '*', '/']
MAX = -1000000001
MIN = 1000000001
symbols = []
for count, sym in zip(symbol_counts, SYM):
    for j in range(count):
        symbols.append(sym)
        
for syms in perms(symbols):
    temp = calculate(nums[0], nums[1], syms[0])
    for i in range(2, n):
        temp = calculate(temp, nums[i], syms[i-1])
    if temp > MAX:
        MAX = temp
    if temp < MIN:
        MIN = temp

print(MAX)
print(MIN)
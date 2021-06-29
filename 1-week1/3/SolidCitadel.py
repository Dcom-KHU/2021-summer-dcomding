from operator import add, sub, mul
from itertools import permutations

n = int(input())
arr = list(map(int, input().split(' ')))
a, b, c, d = map(int, input().split(' '))

maxi, mini = -10**9, 10**9
for ops in permutations([add]*a + [sub]*b + [mul]*c + [lambda x, y: x//y if x>0 else -(abs(x)//y)]*d):
    s = arr[0]
    for i, op in zip(arr[1:], ops):
        s = op(s, i)
    maxi, mini = max(s, maxi), min(s, mini)
    
print(maxi)
print(mini)

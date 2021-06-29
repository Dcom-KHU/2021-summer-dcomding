from operator import add, sub, mul

mydiv = lambda x, y: x//y if x>0 else -(abs(x)//y)

n = int(input())
arr = list(map(int, input().split(' ')))
a, b, c, d = map(int, input().split(' '))

maxi = arr[0]
for i, op in zip(arr[1:], [sub]*b + [mydiv]*d + [add]*a + [mul]*c):
    maxi = op(maxi, i)
print(maxi)

mini = arr[0]
for i, op in zip(arr[1:], [add]*a + [mydiv]*d + [sub]*b + [mul]*c if d else [mul]*c + [add]*a + [mydiv]*d + [sub]*b):
    mini = op(mini, i)
print(mini)

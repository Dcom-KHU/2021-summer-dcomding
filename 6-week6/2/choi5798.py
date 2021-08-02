a, b = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
print(len(A.symmetric_difference(B)))
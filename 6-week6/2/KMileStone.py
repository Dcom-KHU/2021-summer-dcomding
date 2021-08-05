a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))


print(len(A.symmetric_difference(B)))

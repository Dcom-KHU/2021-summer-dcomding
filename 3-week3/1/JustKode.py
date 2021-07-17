n, k = map(int, input().split())
set_var = set(map(int, input().split()))
print(min(len(set_var), k))
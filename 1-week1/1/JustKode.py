from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
list_var = sorted(list(map(int, stdin.readline().split())))

sum_var = 0
for i in range((k + 1) // 2, n - k // 2):
    sum_var += list_var[i]

print(sum_var)
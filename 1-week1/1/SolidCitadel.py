n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

print(sum(sorted(arr)[k//2+k%2:n-(k//2)]))

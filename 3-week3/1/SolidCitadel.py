n, k = map(int, input().split())
books = list(map(int, input().split()))
num = len(set(books))
print(k if num > k else num)

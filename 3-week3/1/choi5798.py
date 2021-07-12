n, k = map(int, input().split())
books = list(map(int, input().split()))

kinds = set(books)
if len(kinds) >= k:
    print(k)
else:
    print(len(kinds))
n, k = map(int, input("").split())
books = list(map(int, input("").split()))

bookset = len(set(books))

print(min(bookset, k))
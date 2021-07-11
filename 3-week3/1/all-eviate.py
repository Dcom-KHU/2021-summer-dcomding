n, k = map(int, input("").split())
books = list(map(int, input("").split()))

bookset = set(books)

print(min(len(bookset), k))
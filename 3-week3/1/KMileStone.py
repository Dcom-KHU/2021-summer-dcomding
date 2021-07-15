n, k = map(int, input().split())
books = list(map(int, input().split()))


max = 0
n_book = len(set(books))

# if num of book class > k, you can get k books
if n_book > k:
    max = k
# else, you can get num of book class
else:
    max = n_book

print(max)

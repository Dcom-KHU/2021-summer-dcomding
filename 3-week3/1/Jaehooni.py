n, k = map(int, input().split())
books = map(int, input().split())
    
book_list = list(set(books))
number_of_book = len(book_list)

if (k > number_of_book):
    print(number_of_book)
    
else:
    print(k)
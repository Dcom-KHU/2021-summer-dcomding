n, k = map(int, input().split())
l = len(list(set(map(int, input().split()))))
    
# TYPE_BOOK = len(list(set(books)))
print(l) if k > l else print(k)
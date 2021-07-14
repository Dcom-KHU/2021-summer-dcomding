n, k = map(int, input().split())
l = len(list(set(map(int, input().split()))))
    
print(l) if k > l else print(k)
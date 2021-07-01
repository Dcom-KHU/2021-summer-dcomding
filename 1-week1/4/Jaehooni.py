import heapq

length, maxDistance = map(int, input().split())
stonesNumber = list(map(int,input().split()))
min_in_max_nums = float('inf')

for i in range(0, len(stonesNumber)-maxDistance+1):
    max_heap = []
    for j in range(i, i+maxDistance):
        value = stonesNumber[j]
        heapq.heappush(max_heap, (-value, value))
    
    min_in_max_nums = min(min_in_max_nums, heapq.heappop(max_heap)[1])
            
print(min_in_max_nums)
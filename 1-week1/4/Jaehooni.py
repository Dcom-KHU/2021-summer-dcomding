import heapq

f = open("input.txt", 'r')
f2 = open("input2.txt", 'r')
length, maxDistance = map(int, f2.read().split())
stonesNumber = list(map(int, f.read().split()))
f.close()
f2.close()
min_in_max_nums = float('inf')

for i in range(0, len(stonesNumber)-maxDistance+1):
    max_heap = []
    for j in range(i, i+maxDistance):
        heapq.heappush(max_heap, (-stonesNumber[j], stonesNumber[j]))
    
    min_in_max_nums = min(min_in_max_nums, heapq.heappop(max_heap)[1])
        
print(min_in_max_nums)
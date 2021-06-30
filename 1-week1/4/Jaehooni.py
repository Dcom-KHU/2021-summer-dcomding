length, maxDistance = map(int, input().split())
stonesNumber = list(map(int,input().split()))


entireMin = max(stonesNumber[0:maxDistance+1])

for i in range(0, len(stonesNumber) - maxDistance):
    if (stonesNumber[i] == entireMin and stonesNumber[maxDistance + 1] < entireMin):
        entireMin = stonesNumber[maxDistance + 1]
        
        
print(entireMin + 1)
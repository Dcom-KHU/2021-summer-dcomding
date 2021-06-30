length, maxDistance = map(int, input().split())
stonesNumber = list(map(int,input().split()))

def jump(stonesNumber):
    distance = 1
    max = 1
    
    for i in range(0, length):
        
        stonesNumber[i] -= 1
        
        if (stonesNumber[i] <= 0):
            distance += 1

        else:
            distance = 1
            
        if (distance > max):
            max = distance
                
    return max
            

people = 1

while True:
    
    if (jump(stonesNumber) <= maxDistance):
        print(stonesNumber)
        people += 1
        
    else:
        print(people)
        break
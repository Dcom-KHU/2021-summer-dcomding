from itertools import permutations
from decimal import Decimal as d

input()
numList = list(map(int, input().split()))
add, minus, mult, div = map(int, input().split())
num = add + minus + mult + div
sumList = []

operatorList = []
for i in range(0, add):
    operatorList.append('+')
    
for i in range(0, minus):
    operatorList.append('-')
    
for i in range(0, mult):
    operatorList.append('*')
    
for i in range(0, div):
    operatorList.append('/')
    
operatorCases = list(set((permutations(operatorList, num))))

def calc(numList, operatorCases):
    max = -1000000001
    min = 1000000001
    
    for operatorCase in operatorCases:
        index = 1
        sum = numList[0]
        
        for j in operatorCase:
            
            if (j == '+'):
                sum = d(sum) + d(numList[index])
                
            elif (j == '-'):
                sum = d(sum) - d(numList[index])
                
            elif (j == '*'):
                sum = d(sum) * d(numList[index])
                
            else:
                if (sum < 0):
                    sum = -sum
                    sum = d(sum) // d(numList[index])
                    sum = -sum
                    
                else:
                    sum = d(sum) // d(numList[index])
                    
            index+=1
            
        if (sum > max):
            max = sum
            
        if (sum < min):
            min = sum
            
    return max, min


max, min = calc(numList, operatorCases)
print(f'{int(max)}\n{int(min)}')
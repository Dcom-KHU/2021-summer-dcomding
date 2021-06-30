from itertools import permutations
from decimal import Decimal as d

input()
numList = list(map(int, input().split()))
add, div, mult, div = map(int, input().split())
num = add + div + mult + div
sumList = []

operatorList = []
for i in range(0, add):
    operatorList.append('+')
    
for i in range(0, div):
    operatorList.append('-')
    
for i in range(0, mult):
    operatorList.append('*')
    
for i in range(0, div):
    operatorList.append('/')
    
operatorCases = list(set((permutations(operatorList, num))))

def calc(numList, operatorCases):
    max = -2**31
    min = 2**31
    
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
                sum = d(float(sum)) / d(numList[index])
                
            index+=1
                
        if (sum > max):
            max = sum
            
        if (sum < min):
            min = sum
            
    return max, min


max, min = calc(numList, operatorCases)
print(f'{int(max)}\n{int(min)}')
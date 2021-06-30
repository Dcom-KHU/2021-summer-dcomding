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

print(numList)
print(operatorCases)

def calc(numList, operatorCases):
    max = -1000000001
    min = 1000000001
    
    for operatorCase in operatorCases:
        index = 1
        sum = numList[0]
        
        for j in operatorCase:
            
            if (sum > 10 ** 9 or sum < -10 ** 9):
                index+=1
                continue
            
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
                
        if (sum > max and sum <= 10 ** 9):
            max = sum
            print(f'max = {operatorCase} \n sum = {sum}')
            
        if (sum < min and sum >= -10 ** 9):
            min = sum
            print(f'min = {operatorCase} \n sum = {sum}')
            
    return max, min


max, min = calc(numList, operatorCases)
print(f'{int(max)}\n{int(min)}')
n = int(input())
table = []

for i in range(0, n):
    t, p = map(int, input().split())
    table.append((t,p))
    

def recursive(day):
    sum = 0
    if (day >= len(table)):
        return 0
    
    elif ((day + table[day][0]) > len(table)):
        return recursive(day+1)
    
    else:
        sum = recursive(day+1) if recursive(day+1) > (table[day][1] + recursive(day + table[day][0])) else table[day][1] + recursive(day + table[day][0])
        return sum


print(recursive(0))
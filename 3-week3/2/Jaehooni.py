n = int(input())
table = [tuple(map(int, input().split())) for i in range(n)]

def r(day):
    if (day >= n):
        return 0
    
    elif (day + table[day][0] > n):
        return r(day+1)
    
    else:
        return max(r(day+1), table[day][1] + r(day + table[day][0]))

print(r(0))
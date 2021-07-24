import sys

n = int(input())
times = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: (x[0],x[1]))

def r(index, start):
    if (index >= len(times)):
        return 0

    elif (start > times[index][0]):
        return r(index+1, start)

    else:
        new_start = times[index][1]
        return max(r(index+1, start), 1+r(index+1,new_start))


sys.setrecursionlimit(100000)
print(r(0, times[0][0]))
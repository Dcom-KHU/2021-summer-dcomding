import sys
sys.setrecursionlimit(200000)

n = int(input())
dict_var = {}
current = "DCOM"
result = ["DCOM"]
check = False

def func(key):
    global dict_var, current, result, check, n
    if check:
        return

    if len(result) == n + 1:
        print(' '.join(result))
        check = True
        return

    if key in dict_var:
        for i in range(len(dict_var[key])):
            if not dict_var[key][i][0]:
                dict_var[key][i][0] = True
                result.append(dict_var[key][i][1])
                func(dict_var[key][i][1])
                result.pop()
                dict_var[key][i][0] = False


for i in range(n):
    start, end = input().split()
    if start not in dict_var:
        dict_var[start] = [[False, end]]
    else:
        dict_var[start].append([False, end])

for key in dict_var:
    dict_var[key].sort(key=lambda x: (len(x[1]), x[1]))

func("DCOM")
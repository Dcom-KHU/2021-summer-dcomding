n = int(input())
dict_var = {}

for i in range(n):
    start, end = input().split()
    if start not in dict_var:
        dict_var[start] = [end]
    else:
        dict_var[start].append(end)

for key in dict_var:
    dict_var[key].sort(key=lambda x: (len(x), x))
    dict_var[key].reverse()

current = "DCOM"
result = "DCOM"

for i in range(n):
    current = dict_var[current].pop()
    result += ' ' + current

print(result)
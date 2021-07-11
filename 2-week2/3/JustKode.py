n = int(input())
dict_var = {}

for i in range(n):
    start, end = input().split()
    if start not in dict_var:
        dict_var[start] = [end]
    else:
        dict_var[start].append(end)
    
    if end not in dict_var:
        dict_var[end] = []  # 없는 경우

for key in dict_var:
    dict_var[key].sort(key=lambda x: (len(x), x))

stack = ["DCOM"]
answer = []
while stack:
    top = stack[-1]
    if top not in dict_var or len(dict_var[top]) == 0:
        answer.append(stack.pop())
    else:
        stack.append(dict_var[top].pop(0))

print(' '.join(answer[::-1]))
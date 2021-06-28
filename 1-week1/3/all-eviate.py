n = int(input(""))
nums = input("").split()
for i in range(n):
    nums[i] = int(nums[i])
ops = input("").split()
for i in range(4):
    ops[i] = int(ops[i])

stack = []
history = []

def calc(ind, a, b):
    if ind == 0:
        return a+b
    elif ind == 1:
        return a-b
    elif ind == 2:
        return a*b
    elif ind == 3:
        return int(a/b)

_ops = ops[:]
for i, v in enumerate(ops):
    if v == 0:
        pass
    else:
        _ops[i] -= 1
        stack.append((1, _ops, calc(i, nums[0], nums[1])))
        _ops = ops[:]

while stack:
    d, o, n = stack.pop()
    if not any(o):
        history.append(n)
    else:
        _ops = o[:]
        for i, v in enumerate(o):
            if v == 0:
                pass
            else:
                _ops[i] = _ops[i] - 1
                stack.append((d+1, _ops, calc(i, n, nums[d+1])))
                _ops = o[:]

print(max(history))
print(min(history))
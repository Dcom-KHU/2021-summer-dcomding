import itertools

def cal(h, o):
    res = nums[0]
    for i in range(0,len(o)):
        if o[i] == '0':
            res += nums[i+1]
        elif o[i] == '1':
            res -= nums[i+1]
        elif o[i] == '2':
            res *= nums[i+1]
        elif o[i] == '3':
            if res < 0:
                res = -((-res)//nums[i+1])
            else:
                res = res//nums[i+1]
    h.append(res)

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
perm = []
for i in range(0, 4):
    for j in range(0, ops[i]):
        perm.append(str(i))
perm = list(map(''.join, itertools.permutations(perm, len(perm))))
history = []
perm_set = set(perm)
perm = list(perm_set)
for i in range(len(perm)):
    cal(history, perm[i])

print(max(history))
print(min(history))
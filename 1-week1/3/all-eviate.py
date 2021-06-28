import itertools

def cal(h, o, n):
    res = n[0]
    for i in range(0,len(o)):
        if o[i] == '0':
            res += n[i+1]
        elif o[i] == '1':
            res -= n[i+1]
        elif o[i] == '2':
            res *= n[i+1]
        elif o[i] == '3':
            if res < 0:
                res = -((-res)//n[i+1])
            else:
                res = res//n[i+1]
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
for i in range(0, len(perm)):
    cal(history, perm[i], nums)

print(max(history))
print(min(history))
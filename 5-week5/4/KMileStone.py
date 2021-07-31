n, f, k = map(int, input().split())
cmd = []
for i in range(k):
    c = input().split()
    if c[0] == 'U' or c[0] == 'D':
        cmd.append((c[0], int(c[1])))
    else:
        cmd.append((c[0],))


table = [True for i in range(n)]
cursor = f
undo = []

for c in cmd:
    if c[0] == 'U':
        for i in range(c[1]):
            cursor -= 1
            while not table[cursor]:
                cursor -= 1

    elif c[0] == 'D':
        for i in range(c[1]):
            cursor += 1
            while not table[cursor]:
                cursor += 1

    elif c[0] == 'C':
        table[cursor] = False
        undo.append(cursor)

        # if last row, select prev row
        if cursor == n-1:
            cursor -= 1
            while not table[cursor]:
                cursor -= 1

        # else select next row
        else:
            cursor += 1
            while not table[cursor]:
                cursor += 1

    elif c[0] == 'Z':
        idx = undo.pop()
        table[idx] = True


# print invalid index
for i in range(n):
    if not table[i]:
        print(i)

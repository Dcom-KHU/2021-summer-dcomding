def solution(n, k, cmd):
    answer = list('O'*n)
    table = [i for i in range(n)]
    check_list = [True for _ in range(n)]
    stack = []
    pointer = k
    def up(pointer, n):
        # return pointer - n
        counter = 0
        while counter < n:
            pointer -= 1
            if check_list[pointer] is True:
                counter += 1
        return pointer
    def down(pointer, n):
        # return pointer + n
        counter = 0
        while counter < n:
            pointer += 1
            if check_list[pointer] is True:
                counter += 1
        return pointer
    def cancel(pointer):
        # stack.append([pointer, table[pointer]])
        check_list[pointer] = False
        stack.append(pointer)
        # del table[pointer]
        try:
            while True:
                pointer += 1
                if check_list[pointer] is True:
                    return pointer
        except:
            while True:
                pointer -= 1
                if check_list[pointer] is True:
                    return pointer
    
    def undo():
        # row, number = stack.pop()
        # table.insert(row, number)
        row = stack.pop()
        check_list[row] = True
        
    for command in cmd:
        command = command.split()
        if command[0] == 'U':
            pointer = up(pointer, int(command[1]))
        elif command[0] == 'D':
            pointer = down(pointer, int(command[1]))
        elif command[0] == 'C':
            pointer = cancel(pointer)
        elif command[0] == 'Z':
            undo()
    for idx in stack:
        answer[idx] = 'X'
    return ''.join(answer)

n, f, k = map(int, input().split())
cmd = []
for _ in range(k):
    temp = input()
    cmd.append(temp)

admin = solution(n, f, cmd)
for i in range(len(admin)):
    if admin[i] == 'X':
        print(i)
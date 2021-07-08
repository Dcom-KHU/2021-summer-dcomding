from collections import deque

def correct(bracket_list):
    bracket_stack = []
    
    for i in range(0, len(bracket_list)):
        if (bracket_list[i] == '('):
            bracket_stack.append('(')

        elif (bracket_list[i] == ')'):
            if (len(bracket_stack) == 0):
                return False
            
            value = bracket_stack.pop()
            if (value != '('):
                return False

        elif (bracket_list[i] == '{'):
            bracket_stack.append('{')

        elif (bracket_list[i] == '}'):
            if (len(bracket_stack) == 0):
                return False
            
            value = bracket_stack.pop()
            if (value != '{'):
                return False

        elif (bracket_list[i] == '['):
            bracket_stack.append('[')

        else:
            if (len(bracket_stack) == 0):
                return False
            
            value = bracket_stack.pop()
            if (value != '['):
                return False
        
        # print(bracket_stack)
    if (len(bracket_stack) == 0):
        return True


correct_num = 0
bracket_list = deque(list(input()))
length = len(bracket_list)

for i in range(0, len(bracket_list)):
    if (correct(bracket_list)):
        # print(bracket_list)
        correct_num += 1
        
    # else:
        # print("uu" , bracket_list)
        
    rotate = bracket_list.popleft()
    bracket_list.append(rotate)
    
print(correct_num)
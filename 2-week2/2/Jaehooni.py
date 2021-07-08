from collections import deque

parent = ['(',')']
curly_bracket = ['{','}']
square_bracket = ['[',']']

def correct(bracket_list):
    parent_left = 0
    curly_left = 0
    square_left = 0
    inner = True
    
    for i in range(0, len(bracket_list)):
        if (bracket_list[i] == '('):
            parent_left += 1
            if (curly_left > 0 or square_left > 0):
                inner = True

        elif (bracket_list[i] == ')'):
            parent_left -= 1
            if (parent_left == 0):
                if (curly_left > 0 or square_left > 0 and inner==False):
                    return False

        elif (bracket_list[i] == '{'):
            curly_left += 1
            if (parent_left > 0 or square_left > 0):
                inner = True

        elif (bracket_list[i] == '}'):
            curly_left -= 1
            if (curly_left == 0):
                if (parent_left > 0 or square_left > 0 and inner==False):
                    return False

        elif (bracket_list[i] == '['):
            square_left += 1
            if (parent_left > 0 or curly_left > 0):
                inner = True

        else:
            square_left -= 1
            if (square_left == 0):
                if (parent_left > 0 or curly_left > 0 and inner==False):
                    return False
        
        if (parent_left < 0 or curly_left < 0 or square_left < 0):
            return False
    
    if (parent_left == 0 and curly_left == 0 and square_left == 0):
        print(bracket_list)
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
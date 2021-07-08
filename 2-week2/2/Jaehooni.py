from collections import deque

parent = ['(',')']
curly_bracket = ['{','}']
square_bracket = ['[',']']

def correct(bracket_deq):
    parent_left = False
    curly_left = False
    square_left = False
    
    for i in range(0, len(bracket_list)):
        print(bracket_list[i])
        
        if (bracket_list[i] == '('):
            if (parent_left == True):
                return False
            
            else:
                parent_left == True
            
        elif (bracket_list[i] == ')'):
            if (parent_left == True):
                parent_left == False
            
            else:
                return False
        
        
        if (bracket_list[i] == '{'):
            if (curly_left == True):
                return False
            
            else:
                curly_left == True
            
        elif (bracket_list[i] == '}'):
            if (curly_left == True):
                curly_left == False
            
            else:
                return False
            
        if (bracket_list[i] == '['):
            if (square_left == True):
                return False
            
            else:
                square_left == True
            
        elif (bracket_list[i] == ']'):
            if (square_left == True):
                square_left == False
            
            else:
                return False
            
            
    return True
            

correct_num = 0
bracket_list = deque(list(input()))
length = len(bracket_list)

for i in range(0, len(bracket_list)):
    if (correct(bracket_list)):
        # print(bracket_list)
        correct_num += 1
        
    else:
        # print("uu" , bracket_list)
        
    rotate = bracket_list.popleft()
    bracket_list.append(rotate)
    
print(correct_num)
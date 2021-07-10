num = int(input())
move_list = []
dest_list = []
number_of_stack = 0
alphabet_list = []
first_dest = ""
shortest_start = ()
shortest_start_index = [0]
first = True


for i in range(0, num):
    start, end = input().split(' ')
    # print(start)
    # print(start, end)
    if (start == "DCOM"):
        move_list.append([(start, end)])
        dest_list.append((len(end), end[0], end))
        number_of_stack += 1
        
    else:
        if (first_dest == ""):
            sorted_zipped_list = sorted(zip(dest_list, move_list), key=lambda dest : dest[0])
            # print(sorted_zipped_list, shortest_value)
        
            move_list = [element for _, element in sorted_zipped_list]
            first_dest = move_list[0][0][1]
            shortest_start = move_list[0][0]
            
        
        non_matching = True
            
        if (start == first_dest and not first):
            move_list.append([shortest_start, (start, end)])
            shortest_start_index.append(number_of_stack)
            number_of_stack += 1
            non_matching  = False
            first = False

        for i in range(0, number_of_stack):          
            if (start == move_list[i][-1][1]):
                move_list[i].append((start, end))
                non_matching = False
                break


            else:
                pass


        if (non_matching == True):
            move_list.append([(start,end)])
            number_of_stack += 1
                
        
    
        
    
            
                
        # move_list = [element for _, element in sorted_zipped_list]
        # first_dest = dest[0]
        # smallest_start = move_list[0]
        # print(first_dest, smallest_start, num)
    
        
    
        
#     else:
#         sorted_zipped_list = sorted(zip(dest, move_list))
#         move_list = [element for _, element in sorted_zipped_list]
#         first_dest = dest[0]
#         smallest_start = move_list[0]
#         print(first_dest, smallest_start, num)
#         break
        
        
# for i in range(0, num):
#     start, end = input().split(' ')
#     for i in range(0, number_of_stack):
#         if (start == first_dest):
#             move_list.append([smallest_start])
#             move_list[-1].append((start, end))
#             smallest_start_index.append(number_of_stack)
#             number_of_stack += 1
        
#         if (start == move_list[i][-1][1]):
#             move_list[i].append((start, end))
            
#         else:
#             pass
        
        
for i in range(0, len(move_list)):
    for j in range(0, len(move_list[i])):
        
        if (i == 0 and j == 0):
            print(move_list[i][j][0], end = " ")
        
        print(move_list[i][j][1], end = " ")
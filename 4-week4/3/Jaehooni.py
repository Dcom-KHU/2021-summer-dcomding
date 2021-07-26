n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
        'turn-col  turn-row  move-bottom move-right'
move = [[1,1,0,0],[0,0,1,1],[0,1,0,1],[1,0,1,0]]
robot_init = [0,0,0,0]


def robot_move(list1, list2):
    new_list = []
    for pair in zip(list1, list2):
        new_list.append(pair[0],pair[1])
        
    return new_list

def r(robot):
    move_posiv = [0,1,2,3]
    if (robot[:2] == [n-1,n-1] or robot[2:] == [n-1,n-1]):
        return 0
    
    elif n in robot or (board[robot[0]][robot[1]] or board[robot[2]][robot[3]]):
        return float('inf')
    
    else:
        if (robot[1] > robot[3] or robot[0] == n-1 or board[robot[0][robot[1]+1]]):
            move_posiv.remove(0)
            
        if (robot[0] < robot[2] or robot[2] == n-1 or board[robot[2]+1][robot[3]]):
            move_posiv.remove(1)
            
        if (len(move_posiv) == 2):
            return min(r(robot_move(robot, move[0]))+1, r(robot_move[robot, move[1]]) + 1)
        
        elif (len(move_posiv) == 3):
            return min(r(robot_move(robot, move[0]), robot_move(robot, move[2]), robot_move(robot, move[3]))
        
        
        else:
            return min(robot_move(robot, move[0]), robot_move(robot, move[0]), robot_move(robot, move[1]), robot_move(robot, move[2]), robot_move(robot, move[3]))
        
    
'''
def r(robot):
    if ((n-1,n-1) in robot):
        return 0
    
    
    elif (board[robot[0][0]][robot[0][1]] or board[robot[1][0]][robot[1][1]]):
        return float("inf")
    
    else:
        robot_turn = [(robot[0][0]+1, robot[0][1]+1), (robot[1][0], robot[1][1])]
        robot_right = [(robot[0][0]+1, robot[0][1]), (robot[1][0]+1, robot[1][1])]
        robot_bottom = [(robot[0][0], robot[0][1]+1), (robot[1][0], robot[1][1]+1)]
    return min(r(robot_turn)+1, r(robot_right)+1, r(robot_bottom)+1)
   
 '''

def r(robot):
    robot_turn_column
    robot_turn_row
    robot_go_right
    robot_go_bottom
    
    if (n-1, n-1) in robot:
        return 0
    
    elif (n-1, n) in robot or (n, n-1) in robot:
        return float('inf')
    
    elif ()
print(board)
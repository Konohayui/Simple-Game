"""
This program applies crosshatching (a method for solving sudokus) 
and backtracking 
"""

unsol = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

# find empty cells
def find_empty_cell(unsol):
    for row in range(9):
        for col in range(9):
            if unsol[row][col] == 0:
                return [row, col]
    return False

# determine valid number 
def check_valid(unsol, row, col, num):
    x = y = z = 0
    
    # check row
    for rj in range(9):
        if unsol[row][rj] == num:
            x = 1

    # check column
    for ci in range(9):
        if unsol[ci][col] == num:
            y = 1
    
    # check subgrid
    subgr_row = row - row % 3
    subgr_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if unsol[subgr_row + i][subgr_col + j] == num:
                z = 1
    
    if x + y + z > 0:
        return False # if num has used
    else: return True
    
def solver(unsol):    
    pos = find_empty_cell(unsol)
    if pos != False:
        row = pos[0]
        col = pos[1]
    else: return True # no empty space, problem solved
    
    for num in range(1, 10):
        if check_valid(unsol, row, col, num) == True:
            unsol[row][col] = num
            if solver(unsol):
                return True
        unsol[row][col] = 0
        
    return False
    
#def check(unsol):    
#    pos = find_empty_cell(unsol)   
#    print(pos)     
#    return(check_valid(unsol, pos, 3))
#
#print(check(unsol))

def display(unsol):
    if solver(unsol) == True:
        for row in range(9):
            print(unsol[row])
        return("Solved!")
    else: return("No Solution!")
    
print(display(unsol))



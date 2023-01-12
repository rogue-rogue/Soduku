"""Early soduku game - playable only in terminal 
    """
    
from typing import Optional
import copy

def get_new_puzzle(): 
    """Generates a new puzzle for gameplay. 
    
    Currently just returns one board.
    
    Future developments:  
    Multiple boards, selecting one at random. 
    Alorithmically generated board, one difficulty
    As above but for multiple difficulties 

    Returns:
        list[list[Optional[int]]]
    """
    
    #type currently used for board is list[list[Optional[int]]]
    board =[
        [6,8,5,1,3,2,9,4,7],
        [7,3,4,5,9,8,2,1,6],
        [2,1,9,7,6,4,8,5,3],
        [9,2,6,8,7,1,5,3,4],
        [8,5,1,3,4,9,6,7,2],
        [4,7,3,2,5,6,1,8,9],
        [5,6,8,4,2,7,3,9,1],
        [3,4,2,9,1,5,7,6,8],
        [1,9,7,6,8,3,4,2, None]] 
    return board

def format_board(board) -> None:
    
    """ Converts from list of integers to a string with relevant formatting

    Return:
        String suitable for printing to terminal. 

    """
    formatted_board = ""
    row_counter = 0

    for row in board:
        row_string = ""
        for column, cell in enumerate(row):
            if cell == None: row_string+=(" ")
            else: row_string+=(str(cell))
            if(column ==2 or column ==5):
                row_string+="|"
        formatted_board += row_string+' '+str(row_counter)+'\n'
        if (row_counter == 2 or row_counter == 5): 
            formatted_board += 11*"-"+'\n'
        row_counter += 1
    formatted_board += "\n012 345 678"
    
    return(formatted_board)

def transform_rows(board):
    columns = [[],[],[],[],[],[],[],[],[]]
    grids =[
        [],[],[],
        [],[],[],
        [],[],[]
        ] 
    
    subgrid_counter = 0 #there are 3 subgrid rows in a 3x3 soduku, sometimes called 'bands'. Start at subgrid band 0
    for row_num, row in enumerate(board, start=1):   
        for col, cell in enumerate(row): 
            columns[col].append(cell)
            
            if (col < 3):
                grids[subgrid_counter].append(cell) #first subgrid in band
            elif (col < 6):
                grids[subgrid_counter+1].append(cell) #second subgrid in band
            elif (col < 9):
                grids[subgrid_counter+2].append(cell) #third subgrid in band

        if (row_num%3 == 0):
            subgrid_counter += 3 #move down to next band 

    return columns, grids

def sum_to_45(data): 
        if None in data: 
            return False
        elif (sum(data)!=45): 
            return False
        else: 
            return True
    
def is_won(board):
    """
    Conditions for winning:
    1. filled board with entries (i.e. that no None's remain)
    2. Numbers 1-9 only appear once in each row,
    3. As 2, but for columns
    4. As 3, but for squares
    
    Returns: Bool
    """
    #create new groups from rows
    columns, grids = transform_rows(board)    
    for row in board: 
        if sum_to_45(row): 
            continue
        else: return False
        
    for column in columns: 
        if sum_to_45(column): 
            continue
        else: return False
    
    for subgrid in grids:
        if sum_to_45(subgrid): 
            continue
        else: return False
    
    return True
    


def main():
    """
    Runs the gameplay 
    """
    starting_board = get_new_puzzle()
    
    #create copy to play on without modifying original puzzle
    game_board = copy.deepcopy(starting_board)    
    
    while is_won(game_board) != True: 
        print(format_board(game_board))
        
        #get the user's move
        move_type = input("Press N for new number, D to delete a number, or R to reset the board: ")
        """This can later be changed so that if you click on an empty square, it's equivalent to N
        #if you cleick on a filled square, it's a D
        #if you click reset, its R
        """
        
        if move_type == "N": 
            move = input("What is the row, col, num?: ")
            row = int(move.split()[0])
            col = int(move.split()[1])
            new_value = int(move.split()[2])  
            
            #check validity 
            if game_board[row][col] != None: 
                print("Please make valid move. Number already here.")
                continue #resets to a new turn 
            
        elif move_type == "D":
            move = input("What is the row, col: ")
            row = int(move.split()[0])
            col = int(move.split()[1])
            new_value = None
        
            #check validity
            if starting_board[row][col] != None: 
                print("Please make valid move. You can't remove an original number.")
                continue #resets to a new turn 
        
        elif move_type == "R":
            game_board = copy.deepcopy(starting_board)
            
            #no validity check required
            
        else: 
            print("Please make valid move!")
            continue #resets to a new turn 
            
        #Update board to reflect move if valid
        game_board[row][col] = new_value
        
    print("Congratulations you have won!")
    
if __name__ == "__main__":
    main()
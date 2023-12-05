import structs
import random

def print_board(state):
    for i in range(len(4)):
        for j in range(len(4)):
            print(state.board[i][j].value)


def isGameOver(state):
    for i in range(4):
        for j in range(4):
            if(state.board[i][j].value == 0): #means we have open space still
                return False
            elif(state.board[i][j] == state.board[i][j+1] or state.board[i][j] == state.board[i][j-1] or state.board[i][j] == state.board[i+1][j] or state.board[i][j] == state.board[i-1][j]):
                return False #board is full but things still can be mereged
    print_board()
    print(f"game over : {state.score}")
    return True #meants that nothing else can be done 


def add_number(state,number): #calling this function means that there is available space, make sure to check that before
# choosing a random index for
# row and column.
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while(state.board[r][c] != None): #could pontentially run into infinite loop if we do not be careful
        r = random.randint(0, 3)
        c = random.randint(0, 3)    

    state.board[r][c] = number

def transpose_board(state):
    new_board = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_board[i][j] = state.board[j][i]
        return new_board
        
def compress_board(state): #if the board gets moved left, all pieces should move to the left
    changed = False
    new_board = [[None] * 4 for _ in range(4)]

    for i in range(4):
        pos = 0
        for j in range(4):
            if(state.board[i][j].value != 0):
                new_board[i][pos] = new_board[i][j]
                if(j != pos):
                    change = True
                pos +=1

    return new_board, changed


def merge(state,direction):
    if(direction == 'R'): # will determine what move we just made, so how we should look at the array 
         offsetX = 1
         offsetY = 0
    elif(direction == 'L'):
        offsetX = -1
        offsetY = 0
    elif(direction == 'U'):
        offsetX = 0
        offsetY = 1
    else:
        offsetX = 0
        offsetY = -1
    for i in range(4):
         for j in range(4):
            if(state.board[i][j] == state.board[i+offsetX][j+offsetY]):
                state.board[i+offsetX][j+offsetY] = state.board[i+offsetX][j+offsetY].value * 2
                state.board[i][j].value = 0
     


def reverse(state):
    new_board = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_board[i][j] = state.board[i][j-3].value
    return new_board


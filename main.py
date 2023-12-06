import game_internals
import structs
import random

legalMove = True
gameOver = False
gameBoard = structs.state()
number = random.randint(0,9)

if(number == 4):
    game_internals.add_number(gameBoard.board,4)
else:
    game_internals.add_number(gameBoard.board,2)

while(gameOver == False):
    legalMove = True
    print("please input a move W, A, S, D")
    print(gameBoard)
    direction = input()
    if(direction == 'd'):
        (grid,changed) = game_internals.move_right(gameBoard.board)
        gameBoard.board = grid
    elif(direction == 'a'):
        (grid,changed) = game_internals.move_left(gameBoard.board)
        gameBoard.board = grid
    elif(direction == 'w'):
        (grid,changed) = game_internals.move_up(gameBoard.board)
        gameBoard.board = grid
    elif(direction == 's'):
        (grid,changed) = game_internals.move_down(gameBoard.board)
        gameBoard.board = grid
    else:
        print("not a legal move")
        legalMove = False
    
    if(legalMove == True):
        if(game_internals.isGameOver(gameBoard.board) == True):
            gameOver = True
            break
        else:
            number = random.randint(0,9)
            if(number == 4):
                game_internals.add_number(gameBoard.board,4)
            else:
                game_internals.add_number(gameBoard.board,2)


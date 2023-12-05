import game_internals
import structs

gameOver = True
gameBoard = structs.state()
while(gameOver == False):
    print("please input a move W, A, S, D")
    game_internals.print_board()
    direction = input()
    if(direction == 'D'):
        gameBoard.board = game_internals.moveRight()
    elif(direction == 'A'):
        gameBoard.board = game_internals.moveLeft()
    elif(direction == 'W'):
        gameBoard.board = game_internals.moveUp()
    elif(direction == 'S'):
        gameBoard.board = game_internals.moveDown()
    
    if(game_internals.isGameOver() == True):
        gameOver = True

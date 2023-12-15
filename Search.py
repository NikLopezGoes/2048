import game_internals


def Utility(state,player):
    return None

def isTerminal(state): #loop over all of the nodes and check if not legal moves can be made
    return game_internals.isGameOver(state)

def get_moves(state):
    valid_moves = []
    (grid,changed) = game_internals.move_left(state)
    if(changed == True):
        valid_moves.append("a")
    (grid,changed) = game_internals.move_right(state)
    if(changed == True):
        valid_moves.append("d")
    (grid,changed) = game_internals.move_up(state)
    if(changed == True):
        valid_moves.append("w")
    (grid,changed) = game_internals.move_down(state)
    if(changed == True):
        valid_moves.append("s")
    return valid_moves

def cutoff_test(state, depth):
    if(depth > 3):
        return True
    else:
        return False


def Max_value(state,player,depth):
    if(isTerminal(state) == True or cutoff_test(state, depth) == True ):
        return (None, Utility(state,player))
    
    best_move = None 
    max_value = float('-inf')
    for move in get_moves(state):
        (min_move,min_value) = Min_value(result(state,move), depth+1)
        if(min_value > max_value):
            best_move = max_value
            max_value = min_value
   
    return(best_move,max_value)


def Min_value(state,player,depth):
    if(isTerminal(state) == True or cutoff_test(state, depth) == True ):
        return (None, Utility(state,player))
    best_move = None
    min_value = float('inf')
    for move in get_moves(state):
        (max_move,value) = Max_value(result(state,move), player)
        if value < min_value:
            best_move = max_move
            min_value = value
    return (best_move,min_value)


def expectimax(state, player,depth):
    if(state.type == "chance"):
        expected = 0
        availableMoves = get_moves(state)
        for i in range(len(availableMoves)):
            move,value = expectimax(result(u,r,depth+1), player)
            expected += probaility(move) + value  #not sure how we know what chance node we are currently evaluating
        return (None, expected)
    
    elif (turn(state) == player):
        return Max_value(u,player,depth+1)
    
    else:
        return Min_value(u,player,depth+1)
    return

def result(move,value):
    move,value = expectimax(node,player,0)
    return move

def probaility(number):
    if number == 2:
        return 0.9
    elif number == 4:
        return 0.1
    else:
        return 0

def greedy_search(board): #greedy algorithm will just loop over the possible moves and output highest score at depth 1
    valid_moves = get_moves(board)
    best_move = None
    best_score = 0
    for i in range(len(valid_moves)):
        if(board[i] == 'w'):
            (grid ,changed, result_score) = game_internals.move_up(board)
        elif(board[i] == 'a'):
            (grid,changed,result_score) = game_internals.move_left(board)
            
        elif(board[i] == 's'):
            (grid,changed,result_score ) = game_internals.move_down(board)
        elif(board[i] == 'd'):
            (grid,changed,result_score) = game_internals.move_right(board)
        
        if(result_score >= best_score):
            best_score = result_score
            best_move = board[i]
    
    return best_move

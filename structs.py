class state:
    def __init__(self):
        self.score = 0
        self.board = state.makeboard()
    
    def makeboard():
        board = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                board[i][j] = None
        return board
    def __str__(self):
        for i in range(4):
            print("___________")
            for j in range(4):
                print(f"|{self.board[i][j].value}|")


class node:
    def __init__(self):
        self.value = 0

    
class state:
    def __init__(self):
        self.score = 0
        self.board = state.makeboard()
    
    def makeboard():
        board = [[0] * 4 for _ in range(4)]
        return board
    def __str__(self):
        final = ""
        for i in range(4):
            for j in range(4):
                # print(f"|{self.board[i][j]}|")
                final += f" {self.board[i][j]} "
            final += "\n"
        return final


class node:
    def __init__(self):
        self.value = 0

    
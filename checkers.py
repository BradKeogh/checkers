import numpy as np

class game:
    def __init__(self):
        self.item = 'hello'
        self.newboard()
        self.turn = 2 # set white to have turn at start

    def greeting(self):
        print(self.item)

    def newboard(self):
        "create new board with pieces"
        self.board = np.zeros([10,10]) # clean board

        # black pieces
        self.board[0:1:,::2] = 1
        self.board[1:2:,1::2] = 1
        self.board[2:3:,::2] = 1
        self.board[3:4:,1::2] = 1

        # white pieces
        self.board[-1::,1::2] = 2
        self.board[-2:-1:,::2] = 2
        self.board[-3:-2:,1::2] = 2
        self.board[-4:-3:,::2] = 2

    def make_move(self,start,end):
        "take input and move piece to location"
        # check if position is valid
        # check if new position is valid

class piece:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

class new_with_problems:
    def __init__(self):
        pass

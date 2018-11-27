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
        #### check if new position is valid
        #calc_2_positons
        #(if off board remove option of move)
        #check all white piece positons, if one is in position of movement change the movement to new possible postition (check not off board)
        # check position request to move in list, if yes move, if no return message not possible.
        #

        # make movement on board and update position in pieces.
        # if there was a jump remove other piece.
        return

class piece:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

class new_with_problems:
    def __init__(self):
        pass

import numpy as np

class game:
    def __init__(self):
        #### set dep
        self.turn = 'W' # set white to have turn at
        self.Wpiece = [] # list of white pieces
        self.Bpiece = []

        #### setup board
        self.board = self.newboard()
        self.greeting()

    def greeting(self):
        print('starting game.........')
        return

    def status(self):
        print('GAME STATUS')
        print('White: ',str(len(self.Wpiece)))
        print('Black: ',str(len(self.Bpiece)))
        print(self.board)
        return

    def newboard(self):
        "create new board with pieces"
        board = np.zeros([100]) # clean board


        # white  pieces
        for i in np.arange(0,10,2):
            p = piece(i,'W') # create piece
            self.Wpiece.append(p) # add to list of pieces
            board[i:i+1] = 1 #add_to_board

        # black pieces
        for i in np.arange(91,100,2):
            p = piece(i,'B') # create piece
            self.Bpiece.append(p) # add to list of pieces
            board[i:i+1] = 2 # add_to_board

        # reshape board
        board = board.reshape(10,10)
        return(board)

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
